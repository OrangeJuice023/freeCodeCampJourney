# Request Header Parser Microservice Project

## Introduction

This is a solution for the Request Header Parser Microservice project, part of the freeCodeCamp Back End Development and APIs curriculum. The project aims to create a microservice that extracts and provides information about the client's IP address, preferred language, and user-agent (browser and operating system).

## Project Description

The Request Header Parser Microservice project focuses on building a simple API that extracts specific information from the request headers of incoming HTTP requests. The microservice returns the client's IP address, preferred language, and user-agent information in JSON format.

## Technologies Used

- Node.js: A runtime environment for executing JavaScript code server-side.
- Express.js: A web application framework for building APIs and handling routes.
- dotenv: A module for loading environment variables from a .env file.
- CORS: Middleware for enabling Cross-Origin Resource Sharing.
  
## How to Run the Project

1. Clone or download this repository to your local machine.
2. Navigate to the project directory using your terminal.
3. Install the required dependencies by running: `npm install`.
4. Create a `.env` file in the project directory and set your preferred port (e.g., `PORT=3000`).
5. Start the server by running: `node index.js`.
6. Access the microservice by opening your browser and navigating to: `http://localhost:3000/api/whoami`.

## API Endpoint

- `GET /api/whoami`: Retrieves information about the client's IP address, preferred language, and user-agent. Responds with the extracted information in JSON format.

## Acknowledgements

This project is part of the freeCodeCamp Back End Development and APIs curriculum. The curriculum and challenges can be found at [freeCodeCamp](https://www.freecodecamp.org/learn/back-end-development-and-apis/).

## Author

Aspiring Programmer (OrangeJuice023)
