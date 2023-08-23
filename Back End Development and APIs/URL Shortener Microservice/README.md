# URL Shortener Microservice Project

## Introduction

This is a solution for the URL Shortener Microservice project, part of the freeCodeCamp Back End Development and APIs curriculum. The project aims to create a microservice that shortens URLs and provides the ability to redirect users to the original URLs.

## Project Description

The URL Shortener Microservice project focuses on building an API that takes a URL as input, performs a DNS lookup to validate the URL, assigns a short URL to the input URL, and stores the mapping in a database. Users can then use the short URL to be redirected to the original URL.

## Technologies Used

- Node.js: A runtime environment for executing JavaScript code server-side.
- Express.js: A web application framework for building APIs and handling routes.
- MongoDB: A NoSQL database used to store URL mappings.
- dns: A built-in Node.js module for DNS lookups.
- urlparser: A module to parse URLs and extract hostname.
- dotenv: A module for loading environment variables from a .env file.
- CORS: Middleware for enabling Cross-Origin Resource Sharing.

## How to Run the Project

1. Clone or download this repository to your local machine.
2. Navigate to the project directory using your terminal.
3. Install the required dependencies by running: `npm install`.
4. Create a `.env` file in the project directory and set your preferred port and MongoDB connection string (e.g., `PORT=3000` and `DB_MAIN=mongodb://localhost:27017`).
5. Start the server by running: `node index.js`.
6. Access the microservice by opening your browser and navigating to: `http://localhost:3000`.

## API Endpoints

- `POST /api/shorturl`: Shortens the provided URL, performs DNS lookup, and stores the mapping in the database. Responds with the original URL and short URL.
- `GET /api/shorturl/:short_url`: Redirects the user to the original URL associated with the provided short URL.

## Acknowledgements

This project is part of the freeCodeCamp Back End Development and APIs curriculum. The curriculum and challenges can be found at [freeCodeCamp](https://www.freecodecamp.org/learn/back-end-development-and-apis/).

## Author

Aspiring Programmer (OrangeJuice023)
