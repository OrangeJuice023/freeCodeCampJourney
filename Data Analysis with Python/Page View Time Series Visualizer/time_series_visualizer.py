import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Register converters for matplotlib
register_matplotlib_converters()

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index('date', inplace=True)

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.lineplot(data=df, x='date', y='value', ax=ax)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Monthly average page views
    df_bar = df.resample('M').mean()
    
    # Handle missing months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['Year'] = df_bar.index.year
    df_bar = df_bar.pivot_table(index='Year', columns='Month', values='value', fill_value=0)
    df_bar = df_bar.reindex(columns=months)
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.barplot(data=df_bar, ax=ax)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title='Months', loc='upper left')
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = df_box['date'].dt.year
    df_box['Month'] = df_box['date'].dt.strftime('%b')
    
    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(data=df_box, x="Year", y="value", ax=axes[0])
    sns.boxplot(data=df_box, x="Month", y="value", ax=axes[1], order=months)
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    fig.tight_layout()
    fig.savefig('box_plot.png')
    return fig

# Call the functions to generate the visualizations
draw_line_plot()
draw_bar_plot()
draw_box_plot()
