#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"

echo -e "\n~~~~~ MY SALON ~~~~~\n"
echo -e "Welcome to My Salon, how can I help you?\n"

# Function to display the numbered list of services
display_services() {
  echo "Services available:"
  $PSQL "SELECT service_id, name FROM services ORDER BY service_id" | while IFS=$'\t' read -r service_id name; do
    echo "${service_id}) ${name}"
  done
}

# Function to get valid service_id from the user
get_service_id() {
  read -p "Enter the service_id: " SERVICE_ID_SELECTED

  # Check if the service_id is a number and exists in the services table
  result=$($PSQL "SELECT COUNT(*) FROM services WHERE service_id = ${SERVICE_ID_SELECTED}")

  if [[ "$result" -eq 1 ]]; then
    return
  else
    echo "Invalid service_id. Please choose a valid service from the list."
    get_service_id
  fi
}

get_service_id

# Function to get customer's name and phone number
get_customer_info() {
  read -p "What's your phone number? " CUSTOMER_PHONE

  # Check if the phone number exists in the customers table
  result=$($PSQL "SELECT customer_id, name FROM customers WHERE phone='$CUSTOMER_PHONE'")
  CUSTOMER_INFO=($result)
  CUSTOMER_ID=${CUSTOMER_INFO[0]}
  CUSTOMER_NAME=${CUSTOMER_INFO[1]}

  if [[ -z "$CUSTOMER_NAME" ]]; then
    read -p "I don't have a record for that phone number, what's your name? " CUSTOMER_NAME
    $PSQL "INSERT INTO customers(name, phone) VALUES ('$CUSTOMER_NAME', '$CUSTOMER_PHONE') RETURNING customer_id"
    CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$CUSTOMER_PHONE'")
  fi
}

get_customer_info

# Function to prompt for appointment time and insert the appointment into the database
make_appointment() {
  echo "What time would you like your $(display_services | grep "$SERVICE_ID_SELECTED")?"
  read SERVICE_TIME

  $PSQL "INSERT INTO appointments(customer_id, service_id, time) VALUES ('$CUSTOMER_ID', '$SERVICE_ID_SELECTED', '$SERVICE_TIME')"

  echo -e "\nI have put you down for a $(display_services | grep "$SERVICE_ID_SELECTED") at $SERVICE_TIME, $CUSTOMER_NAME."
}

make_appointment
