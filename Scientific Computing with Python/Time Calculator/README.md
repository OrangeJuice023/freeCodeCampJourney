# Add Time Calculator

## Overview

As part of the Scientific Computing with Python curriculum on FreeCodeCamp, I developed the "Add Time Calculator." This Python function calculates the time after adding a specified duration to a given start time. It also supports consideration of days of the week.

## Function Details

The `add_time` function takes three main inputs:
- `start`: The starting time in the format "hh:mm AM/PM".
- `duration`: The duration to be added in the format "h:mm".
- `day_of_week` (optional): The day of the week (case-insensitive) to consider.

The function returns the new time in the same format as the input time, along with optional information about the day of the week and the number of days added.

## Key Features

The `add_time` function encompasses the following features:
- Time Calculation: The function calculates the new time by adding the specified duration to the input start time.
- AM/PM Flipping: If the sum of hours and duration results in an AM/PM flip, the function adjusts the AM/PM accordingly.
- Day Consideration: When provided, the function takes the day of the week into account and updates it based on the number of days added.
- Next Day and Multiple Days: The function identifies and formats when the resulting time is on the next day or multiple days later.

## Learning Outcome

Working on the "Add Time Calculator" project provided me with:
- **Time Manipulation:** I enhanced my ability to manipulate time data and calculate time intervals.
- **Conditional Logic:** I practiced using conditional statements to handle AM/PM flips and day adjustments.
- **Function Design:** I gained experience in designing a Python function that performs calculations and produces meaningful outputs.


Happy coding! 💻🚀
