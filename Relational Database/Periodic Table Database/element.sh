#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

SYMBOL=$1

if [[ -z $SYMBOL ]]; then
  echo "Please provide an element as an argument."
else 
  if [[ ! $SYMBOL =~ ^[0-9]+$ ]]; then
    # if input is not a number, check if it's a full name
    LENGTH=$(echo -n "$SYMBOL" | wc -m)
    if [[ $LENGTH -gt 2 ]]; then
      # get data by full name
      QUERY="SELECT * FROM elements INNER JOIN properties USING(atomic_number) INNER JOIN types USING (type_id) WHERE name='$SYMBOL'"
    else
      # get data by atomic symbol
      QUERY="SELECT * FROM elements INNER JOIN properties USING(atomic_number) INNER JOIN types USING (type_id) WHERE symbol='$SYMBOL'"
    fi
  else
    # get data by atomic number
    QUERY="SELECT * FROM elements INNER JOIN properties USING(atomic_number) INNER JOIN types USING (type_id) WHERE atomic_number=$SYMBOL"
  fi

  # Execute the query and process the result
  DATA=$($PSQL "$QUERY")
  if [[ -z $DATA ]]; then
    echo "I could not find that element in the database."
  else
    while read -r BAR BAR NUMBER BAR SYMBOL BAR NAME BAR WEIGHT BAR MELTING BAR BOILING BAR TYPE; do 
      echo "The element with atomic number $NUMBER is $NAME ($SYMBOL). It's a $TYPE, with a mass of $WEIGHT amu. $NAME has a melting point of $MELTING celsius and a boiling point of $BOILING celsius."
    done <<< "$DATA"
  fi
fi
