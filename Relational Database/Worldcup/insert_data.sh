#! /bin/bash

if [[ $1 == "test" ]]; then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

GAMES=games.csv

GET_ID() {
  local team_name="$1"
  local team_id=$($PSQL "SELECT team_id FROM teams WHERE name = '$team_name';")
  if [[ -z $team_id ]]; then
    team_id=$($PSQL "INSERT INTO teams(name) VALUES ('$team_name') RETURNING team_id;")
  fi
  echo "$team_id"
}

echo $($PSQL "TRUNCATE games, teams;")

while IFS="," read -r year round winner opponent winner_goals opponent_goals; do
  if [[ $year != "year" ]]; then
    winner_id=$(GET_ID "$winner")
    opponent_id=$(GET_ID "$opponent")

    $PSQL "INSERT INTO games (year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES ($year, '$round', $winner_id, $opponent_id, $winner_goals, $opponent_goals);"
  fi
done < "$GAMES"
