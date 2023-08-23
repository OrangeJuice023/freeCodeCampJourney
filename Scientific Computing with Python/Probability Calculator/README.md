# Probability Calculator

## Hat Class

The `Hat` class represents a collection of colored balls in a hat. It provides methods for initializing the hat with different numbers of balls and for drawing a specified number of balls from the hat.

- `__init__(self, **balls)`: Initializes the hat with balls, where each ball type is specified as a keyword argument with its count.
- `draw(self, num_balls)`: Draws a specified number of balls from the hat, removing them from the contents of the hat. Returns a list of the drawn balls.

## Experiment Function

The `experiment` function simulates an experiment involving drawing balls from a hat and calculates the probability of a certain outcome.

- `experiment(hat, expected_balls, num_balls_drawn, num_experiments)`: Conducts an experiment using the specified parameters.
  - `hat`: An instance of the `Hat` class representing the hat with its contents.
  - `expected_balls`: A dictionary specifying the expected counts of balls for a successful outcome.
  - `num_balls_drawn`: The number of balls drawn from the hat in each experiment.
  - `num_experiments`: The number of experiments to run.
  
The function returns the probability of achieving the expected outcome based on the specified experiment parameters.

## Key Features

- **Hat Class:** The `Hat` class encapsulates the concept of drawing balls from a hat and allows for flexible initialization and drawing.
- **Experiment Simulation:** The `experiment` function simulates drawing balls from the hat multiple times and calculates the probability of achieving the desired outcome.
- **Deep Copy:** The function uses `copy.deepcopy` to create a copy of the hat for each experiment to avoid modifying the original hat.

## Learning Outcomes

Working with the `Hat` class and the `experiment` function enhanced my skills in:

- **Class Design:** I learned how to design a class that simulates drawing items from a container.
- **Probability Simulation:** I practiced creating simulations to estimate probabilities of specific outcomes.
- **Using Libraries:** I used the `copy` and `random` libraries to perform deep copies and generate random numbers.
- **Algorithmic Thinking:** I developed my ability to devise a strategy for conducting multiple experiments and analyzing outcomes.

Happy coding! 💻🚀
