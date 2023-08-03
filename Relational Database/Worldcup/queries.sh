#! /bin/bash

PSQL="psql --username=freecodecamp --dbname=worldcup --no-align --tuples-only -c"

# Do not change code above this line. Use the PSQL variable above to query your database.

# Function to run the query and echo the result with a provided message
run_query() {
  local query="$1"
  local message="$2"
  echo -e "\n$message"
  echo "$($PSQL "$query")"
}

# Queries
run_query "SELECT SUM(winner_goals) FROM games;" "Total number of goals in all games from winning teams:"
run_query "SELECT SUM(winner_goals + opponent_goals) FROM games;" "Total number of goals in all games from both teams combined:"
run_query "SELECT AVG(winner_goals) FROM games;" "Average number of goals in all games from the winning teams:"
run_query "SELECT ROUND(AVG(winner_goals), 2) FROM games;" "Average number of goals in all games from the winning teams rounded to two decimal places:"
run_query "SELECT AVG(winner_goals + opponent_goals) FROM games;" "Average number of goals in all games from both teams:"
run_query "SELECT MAX(winner_goals) FROM games;" "Most goals scored in a single game by one team:"
run_query "SELECT COUNT(*) FROM games WHERE winner_goals > 2;" "Number of games where the winning team scored more than two goals:"
run_query "SELECT name FROM games INNER JOIN teams ON games.winner_id = teams.team_id WHERE round='Final' AND year=2018;" "Winner of the 2018 tournament team name:"
run_query "SELECT name FROM teams WHERE team_id IN (SELECT winner_id FROM games WHERE year=2014 AND round='Eighth-Final') OR team_id IN (SELECT opponent_id FROM games WHERE year=2014 AND round='Eighth-Final') ORDER BY name;" "List of teams who played in the 2014 'Eighth-Final' round:"
run_query "SELECT DISTINCT(name) FROM games INNER JOIN teams ON games.winner_id = teams.team_id ORDER BY name;" "List of unique winning team names in the whole data set:"
run_query "SELECT year, name FROM games INNER JOIN teams ON games.winner_id = teams.team_id WHERE round = 'Final' ORDER BY year;" "Year and team name of all the champions:"
run_query "SELECT name FROM teams WHERE name LIKE 'Co%';" "List of teams that start with 'Co':"
