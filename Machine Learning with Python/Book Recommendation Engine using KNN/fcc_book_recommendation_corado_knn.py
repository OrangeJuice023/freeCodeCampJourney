# -*- coding: utf-8 -*-
"""fcc_book_recommendation_corado_knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16VqU-ru6z9jUCvHkVqOeuwhZ0dMwIOKM
"""

# import libraries (you may add additional imports but you may not have to)
import numpy as np
import pandas as pd
import math
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import matplotlib as mpl
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import magma
import pandas as pd

# get data files
!wget https://cdn.freecodecamp.org/project-data/books/book-crossings.zip

!unzip book-crossings.zip

books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'

import pandas as pd

df_books = pd.read_csv(
    books_filename,
    encoding="ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'}
)

df_ratings = pd.read_csv(
    ratings_filename,
    encoding="ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'}
)

duplicate_isbns = df_books[df_books.duplicated(['title', 'author'], keep=False)]
isbn_mapping = duplicate_isbns.groupby(['title', 'author'])['isbn'].first().to_dict()
df_ratings['isbn'] = df_ratings['isbn'].map(isbn_mapping.get).fillna(df_ratings['isbn'])

duplicate_books = df_books.groupby(['title', 'author']).title.agg(['count']).reset_index().query('count > 1')
duplicates_books_count = duplicate_books['count'].sum() - len(duplicate_books)

duplicate_ratings = df_ratings.groupby(['isbn', 'user']).isbn.agg(['count']).reset_index().query('count > 1')
duplicates_ratings_count = duplicate_ratings['count'].sum() - len(duplicate_ratings)

df_books = df_books.drop_duplicates(subset=['title', 'author'])
df_ratings = df_ratings.drop_duplicates(subset=['isbn', 'user'])

print("Found and removed {:,} duplicate copies of books and {:,} duplicate copies of ratings".format(duplicates_books_count, duplicates_ratings_count))

books_count_before = len(df_books)
books_with_ratings = df_books.merge(df_ratings, on='isbn')
grouped_by_isbn = books_with_ratings.groupby(['isbn', 'title']).rating.agg(['count', 'mean']).reset_index()
books_min_count = 100
acceptable_books = grouped_by_isbn.query('count >= {}'.format(books_min_count))['isbn'].tolist()
grouped_by_isbn = grouped_by_isbn[grouped_by_isbn['isbn'].isin(acceptable_books)]
df_books = df_books[df_books['isbn'].isin(acceptable_books)]
books_count_after = len(df_books)
b_percent_change = round((books_count_before - books_count_after) / books_count_before * 100, 2)
print('Removed {:,} rows ({}%) of books with less than {} reviews'.format(books_count_before - books_count_after, b_percent_change, books_min_count))

users_count_before = len(df_ratings)
ratings_min_count = 200
df_ratings = df_ratings[df_ratings['isbn'].isin(acceptable_books)]
acceptable_users = df_ratings.groupby(['user']).rating.agg(['count']).reset_index().query('count >= {}'.format(ratings_min_count))['user'].tolist()
df_ratings = df_ratings[df_ratings['user'].isin(acceptable_users)]
users_count_after = len(df_ratings)
u_percent_change = round((users_count_before - users_count_after) / users_count_before * 100, 2)
print('Removed {:,} rows ({}%) of user ratings with less than {} reviews per account or invalid books'.format(users_count_before - users_count_after, u_percent_change, ratings_min_count))

grouped_by_user = df_ratings.groupby(['user'])
user_ratings = grouped_by_user['rating'].agg(['sum', 'count', 'mean']).reset_index()

user_count = len(grouped_by_user['user'])
review_count = len(df_ratings)
most_active_list = user_ratings.sort_values(by='count')
most_active_user = most_active_list.iloc[-1]

print('--- BASIC STATS\n')
print('There is over {:,} reviews in the database written by {:,} users'.format(review_count, user_count))
print('The most active user (ID: #{}) has written {:,} reviews\n'.format(most_active_user.name, int(most_active_user['count'])))

print('\n--- WHERE DO MOST OF OUR REVIEWS COME FROM?\n')
SLICE_NUMBERS = 5
step_size = int(user_count / SLICE_NUMBERS)
percentile = int(100 / SLICE_NUMBERS)
labels_percentile = ['{}%-{}%'.format(100-(n*percentile), 100-((n+1)*percentile)) for n in range(SLICE_NUMBERS)]
count_per_percentile = []
quartile = [round(((n+1)*percentile/100)-0.2, 1) for n in range(SLICE_NUMBERS+1)]
reviews_distribution = most_active_list['count'].groupby(
    pd.qcut(most_active_list['count'].rank(method='first'), q=quartile)
).sum()
most_active_list['distribution'] = reviews_distribution

fig = plt.figure(figsize=(8,4))
ax = fig.add_axes([1,0,1,1])
ax.bar(labels_percentile, reviews_distribution.tolist())
plt.title('Which user group contributes the most?')
plt.xlabel('Percentile')
plt.ylabel('Reviews')
plt.show()

top_reviewers_count = most_active_list.iloc[-step_size:]['count'].sum()
print('\nThe top {}% of users contributed to {}% of reviews'.format(percentile, round(top_reviewers_count/review_count*100,2)))

print("\n--- HOW MANY REVIEWS DO USERS USUALLY LEAVE?\n")
binned = pd.cut(user_ratings['count'], bins=[0,100,200,500,1000])
ax = binned.value_counts(sort=False).plot.bar(rot=0, figsize=(8,4))
ax.set_xticklabels(["{} to {}".format(c.left, c.right) for c in binned.cat.categories])
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('How many reviews does each user have?')
plt.ylabel("Users")
plt.xlabel("# of reviews per account")
plt.show()

LOW_COUNT_THRESOLD = 10
inactive_users = user_ratings[user_ratings['count'] < LOW_COUNT_THRESOLD]
inactive_count = len(inactive_users)
inactive_percentage = round(inactive_count/user_count*100,2)

print("\n--- WHAT IS THE RELATIONSHIP B/T ENGAGEMENT RATE AND AVERAGE REVIEW SCORES?\n")
score_distribution = most_active_list['mean'].groupby(
    pd.qcut(most_active_list['count'].rank(method='first'), q=quartile)
).mean()
fig, ax = plt.subplots(figsize=(8,4))
ax.bar(labels_percentile, reviews_distribution.tolist())
ax2 = ax.twinx()
ax2.plot(labels_percentile, score_distribution.tolist(), color = 'red')
ax.set_xlabel('Percentile')
ax.set_ylabel('Review count')
ax2.set_ylabel('Avg rating')
ax2.set_ylim(0,10)

plt.title('Review sentiment across active percentile?')
plt.xlabel('Review count')
plt.show()

score_range = (0, 6)
reviews_within_range = df_ratings.query('{} <= rating <= {}'.format(score_range[0], score_range[1]))
within_range_count = len(reviews_within_range)
within_range_percent = round(within_range_count/review_count * 100, 2)
avg = df_ratings['rating'].mean()
print('\nThe average review is {0:.2f}'.format(avg))

print("\n--- WHAT REVIEW SCORES ARE MOST OFTEN POSTED ON THE SITE?\n")

grouped_by_score = df_ratings.groupby(['rating']).count()
scores = df_ratings['rating'].unique().tolist()
scores.sort()
fig = plt.figure(figsize=(8,4))
ax = fig.add_axes([1,0,1,1])
colors = ['#FF0000','#FF3300', '#ff6600', '#ff9900', '#FFCC00','#FFFF00', '#ccff00', '#99ff00', '#66ff00', '#33ff00', '#00FF00']
ax.bar(scores, grouped_by_score['user'], color=colors)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('What review score is most popular?')
plt.xlabel('Score')
plt.ylabel('Reviews')
plt.show()

low_score_threshold = 2
reviews_within_range = df_ratings.query('rating < {}'.format(low_score_threshold))
within_range_count = len(reviews_within_range)
within_range_percent = round(within_range_count/review_count * 100, 2)
avg = df_ratings['rating'].mean()
print('\nThe global review average is {0:.2f}'.format(avg))

HATER_THRESHOLD = 3
haters = user_ratings[user_ratings['mean'] < HATER_THRESHOLD]
haters_count = len(haters)
hater_percentage = round(haters_count/user_count*100,2)
print('\nThere are {:,} users ({}%) who\'s average review is lower than {}'.format(haters_count, hater_percentage, HATER_THRESHOLD))



import pandas as pd
from scipy.sparse import csr_matrix

df_books = pd.read_csv(
    books_filename,
    encoding="ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'}
)

df_ratings = pd.read_csv(
    ratings_filename,
    encoding="ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'}
)

df = df_ratings
counts1 = df['user'].value_counts()
counts2 = df['isbn'].value_counts()

df = df[~df['user'].isin(counts1[counts1 < 200].index)]
df = df[~df['isbn'].isin(counts2[counts2 < 100].index)]

merged_df = pd.merge(right=df, left=df_books, on="isbn")
merged_df = merged_df.drop_duplicates(subset=["title", "user"])

books_features_pivot = merged_df.pivot(
    index='title',
    columns='user',
    values='rating'
).fillna(0)

mat_books_features = csr_matrix(books_features_pivot.values)

import numpy as np
from sklearn.neighbors import NearestNeighbors

def get_recommends(book="", n=5):
    pivot = books_features_pivot
    titles = list(pivot.index.values)
    data = pivot.values

    def title_2_index(title):
        ind = titles.index(title)
        return data[ind, :]

    def index_2_title(ind):
        return titles[ind]

    model = NearestNeighbors(metric="cosine", algorithm="brute", p=2)
    model.fit(data)

    idx = title_2_index(book)
    distances, indices = model.kneighbors(np.reshape(idx, [1, -1]), n_neighbors=n + 1)

    raw_recommends = sorted(
        list(
            zip(
                indices.squeeze().tolist(),
                distances.squeeze().tolist()
            )
        ),
        key=lambda x: x[1]
    )[1:]

    recommended_books = []
    print('Recommendations for {}:'.format(book))
    for i, (idx, dist) in enumerate(raw_recommends):
        dist = dist
        recommended_books.append([index_2_title(idx), dist])
        print('{0}: {1}, with distance of {2:,.2f}'.format(i + 1, index_2_title(idx), dist))
    print('-----------------')
    return [book, recommended_books]

def test_book_recommendation():
  test_pass = True
  recommends = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))", 10)
  if recommends[0] != "Where the Heart Is (Oprah's Book Club (Paperback))":
    test_pass = False
  recommended_books = ["I'll Be Seeing You", 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True', 'The Lovely Bones: A Novel']
  recommended_books_dist = [0.8, 0.77, 0.77, 0.77, 0.72]
  recommended_books.reverse()
  recommended_books_dist.reverse()

  for i in range(2):
    if recommends[1][i][0] not in recommended_books:
      test_pass = False
    if abs(recommends[1][i][1] - recommended_books_dist[i]) >= 0.05:
      test_pass = False
  if test_pass:
    print("You passed the challenge! 🎉🎉🎉🎉🎉")
  else:
    print("You haven't passed yet. Keep trying!")

test_book_recommendation()