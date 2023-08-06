#!/bin/bash

# Function to execute a PSQL query
function run_psql_query {
    local query=$1
    psql --username=freecodecamp --dbname=number_guess -t --no-align -c "$query"
}

echo "Enter your username:"
read USERNAME

USERNAME_AVAIL=$(run_psql_query "SELECT username FROM users WHERE username='$USERNAME'")
GAMES_PLAYED=$(run_psql_query "SELECT COUNT(*) FROM users INNER JOIN games USING(user_id) WHERE username='$USERNAME'")
BEST_GAME=$(run_psql_query "SELECT MIN(number_guesses) FROM users INNER JOIN games USING (user_id) WHERE username='$USERNAME'")

echo "GAMES_PLAYED: $GAMES_PLAYED"
echo "BEST_GAME: $BEST_GAME"

if [[ -z $USERNAME_AVAIL ]]; then
    run_psql_query "INSERT INTO users(username) VALUES('$USERNAME')"
    echo "Welcome, $USERNAME! It looks like this is your first time here."
else
    echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
fi

RANDOM_NUM=$((1 + $RANDOM % 1000))
GUESS=1
echo "Guess the secret number between 1 and 1000:"

while read NUM; do
    if [[ ! $NUM =~ ^[0-9]+$ ]]; then
        echo "That is not an integer, guess again:"
    else
        if [[ $NUM -eq $RANDOM_NUM ]]; then
            break;
        else
            if [[ $NUM -gt $RANDOM_NUM ]]; then
                echo -n "It's lower than that, guess again:"
            elif [[ $NUM -lt $RANDOM_NUM ]]; then
                echo -n "It's higher than that, guess again:"
            fi
        fi
    fi
    GUESS=$((GUESS + 1))
done

if [[ $GUESS == 1 ]]; then
    echo "You guessed it in $GUESS try. The secret number was $RANDOM_NUM. Nice job!"
else
    echo "You guessed it in $GUESS tries. The secret number was $RANDOM_NUM. Nice job!"
fi

USER_ID=$(run_psql_query "SELECT user_id FROM users WHERE username = '$USERNAME'")
run_psql_query "INSERT INTO games(number_guesses, user_id) VALUES($GUESS, $USER_ID)"
