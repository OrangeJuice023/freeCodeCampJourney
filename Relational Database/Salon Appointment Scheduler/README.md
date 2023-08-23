# Salon Scheduler Activity

## Introduction

The Salon Scheduler activity provides hands-on experience in building a simple appointment scheduling system for a salon using a PostgreSQL database and a bash script. This README document outlines my interaction with the provided bash script to manage appointments, services, and customer information.

## Script Overview

The provided bash script simulates a salon scheduling application. The script allows customers to select services, provide their information, and book appointments. The script interacts with the PostgreSQL database using SQL queries to manage data related to services, customers, and appointments.

## User Interaction

Upon execution, the script greets users with a welcome message and displays a list of available services. Users can choose a service by entering the corresponding service ID. The script ensures that the entered service ID is valid before proceeding.

The script then prompts users for their phone number and checks if the customer's information is already in the database. If the customer is not registered, they are prompted to provide their name, and the information is added to the customers table.

After collecting customer information, the script prompts users for their preferred appointment time and inserts the appointment details into the appointments table.

## Database Interaction

The script uses the `psql` command-line tool to interact with the PostgreSQL database. It executes SQL queries to retrieve and update information related to services, customers, and appointments.

## Script Workflow

1. Display services: The script displays a numbered list of available services for users to choose from.

2. Get service ID: Users enter a service ID, and the script verifies its validity by querying the services table.

3. Get customer info: Users provide their phone number, and the script checks if the customer exists in the customers table. If not, the script prompts for the customer's name and inserts a new customer record.

4. Make appointment: Users choose an appointment time for the selected service, and the script inserts the appointment details into the appointments table.

## Real-World Application

The Salon Scheduler activity replicates the process of managing appointments and customer information in a salon setting. This practice is relevant not only for salons but also for businesses that require appointment scheduling and customer relationship management.

## Conclusion

Engaging with the Salon Scheduler activity allowed me to apply relational database concepts in a practical scenario. The bash script's integration with the PostgreSQL database showcases the power of SQL queries in managing and retrieving data for an appointment scheduling system.

The experience gained from this activity is transferable to various industries where data management and user interaction are essential. From salons to healthcare facilities, the principles learned in this activity can be adapted for diverse applications.
