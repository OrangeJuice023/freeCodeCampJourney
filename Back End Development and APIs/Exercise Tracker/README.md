# Exercise Tracker Project

## Introduction

This is a solution for the Exercise Tracker project, part of the freeCodeCamp Back End Development and APIs curriculum. The project involves creating an API for managing user information, exercise logs, and retrieving exercise logs with filtering options.

## Project Description

The Exercise Tracker project focuses on building a RESTful API using Express and MongoDB to manage user information and exercise logs. Users can create accounts, log exercises, and retrieve their exercise logs with optional filtering by date range and limit.

## Technologies Used

- Node.js: A runtime environment for executing JavaScript code server-side.
- Express.js: A web application framework for building APIs and handling routes.
- MongoDB: A NoSQL database used to store user information and exercise logs.
- Mongoose: An Object Data Modeling (ODM) library for MongoDB and Node.js.
- CORS: Middleware for enabling Cross-Origin Resource Sharing.

## How to Run the Project

1. Clone or download this repository to your local machine.
2. Navigate to the project directory using your terminal.
3. Install the required dependencies by running: `npm install`.
4. Create a `.env` file in the project directory and set your MongoDB connection string (e.g., `DB_URL=mongodb://localhost/exercisetracker`).
5. Start the server by running: `node index.js`.
6. Access the API by sending HTTP requests to the specified endpoints.

## API Endpoints

- `GET /api/users`: Fetches a list of users.
- `POST /api/users`: Creates a new user.
- `POST /api/users/:_id/exercises`: Logs an exercise for a specific user.
- `GET /api/users/:_id/logs`: Fetches exercise logs for a specific user with optional filtering.

## Acknowledgements

This project is part of the freeCodeCamp Back End Development and APIs curriculum. The curriculum and challenges can be found at [freeCodeCamp](https://www.freecodecamp.org/learn/back-end-development-and-apis/).

## Author

Aspiring Programmer (OrangeJuice023)
