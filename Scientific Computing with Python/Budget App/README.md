# Budget Tracker

## Category Class

The `Category` class is designed to help track and manage budget categories. It includes the following methods:

- `__init__(self, description)`: Initializes a budget category with a description and an empty ledger.
- `deposit(self, amount, description="")`: Adds a deposit to the ledger and increases the category's balance.
- `withdraw(self, amount, description="")`: Records a withdrawal in the ledger and decreases the category's balance if sufficient funds are available.
- `get_balance(self)`: Returns the current balance of the category.
- `transfer(self, amount, category_instance)`: Transfers funds from one category to another if sufficient funds are available.
- `check_funds(self, amount)`: Checks if the category has enough funds for a specified amount.

## create_spend_chart Function

The `create_spend_chart` function generates a bar chart to visualize the percentage of spending in different budget categories. It takes a list of `Category` instances as input. The function performs the following steps:

1. Calculate the total amount spent in each category and the percentage spent.
2. Create the bar chart using the calculated percentages, displaying a horizontal bar for each category.
3. Add category descriptions below the chart.

## Key Features

- **Category Tracking:** The `Category` class helps track financial transactions and balances for different budget categories.
- **Deposits and Withdrawals:** The class supports recording deposits and withdrawals, along with balance adjustments.
- **Transfers:** The `transfer` method allows transferring funds between categories.
- **Visualizing Spending:** The `create_spend_chart` function visualizes spending patterns across different budget categories using a bar chart.

## Learning Outcomes

Working with the `Category` class and the `create_spend_chart` function taught me:
- **Object-Oriented Programming:** I learned how to design and implement a class to manage budget categories and transactions.
- **Data Visualization:** I gained experience in generating a bar chart to visually represent data using plain text.
- **Mathematical Calculations:** I practiced calculating percentages and creating a visual representation based on those calculations.

Happy coding! 💻🚀
