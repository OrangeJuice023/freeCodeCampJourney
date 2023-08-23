# Periodic Table Activity

## Introduction

The Periodic Table activity involves building a command-line tool that interacts with a PostgreSQL database containing information about chemical elements. The provided bash script allows users to retrieve details about elements by their atomic number, atomic symbol, or full name. This README provides an overview of my experience using the script to access and display information from the periodic table database.

## Script Overview

The bash script interacts with the PostgreSQL database using the `psql` command-line tool. It provides users with the ability to query element data by atomic number, atomic symbol, or full name. The script supports multiple types of input and adapts its query based on the provided information.

## User Interaction

Upon execution, the script expects an argument containing either the atomic number, atomic symbol, or full name of an element. Depending on the input type, the script constructs a corresponding SQL query to retrieve relevant information from the periodic table database.

If no argument is provided, the script prompts users to provide an element as an argument.

## Database Interaction

The script's primary interaction with the database involves executing SQL queries to retrieve data about chemical elements. The script performs joins with other tables to fetch comprehensive information about each element, including its properties and classification.

## Script Workflow

1. Argument Handling: The script accepts an argument from the command line, which can be an atomic number, atomic symbol, or full name of an element.

2. Query Construction: Based on the argument type, the script constructs an appropriate SQL query to retrieve element data from the database.

3. Query Execution: The script executes the constructed query using the `psql` command-line tool.

4. Result Processing: If the query returns valid data, the script processes and formats the information to provide a detailed description of the element, including its name, symbol, atomic number, type, mass, melting point, and boiling point.

## Real-World Application

The Periodic Table activity demonstrates the application of relational databases in organizing and retrieving information efficiently. This type of tool could be used in educational settings, research environments, or industrial laboratories to quickly access essential information about chemical elements.

## Conclusion

Participating in the Periodic Table activity allowed me to practice working with a real-world database and creating a command-line tool to access specific information. The script's ability to handle different types of inputs and construct tailored queries showcases the flexibility and power of SQL queries.

The experience gained from this activity is transferable to various fields, including science, education, and research, where quick and accurate access to data is crucial. Through this activity, I learned not only about databases and SQL but also about the practical applications of data management in various contexts.
