# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # Append the previous play to the opponent's history
    opponent_history.append(prev_play)

    # If it's the first move of the game, play randomly
    if prev_play == "":
        import random
        return random.choice(["R", "P", "S"])

    # Initialize the guess to "R" as a default
    guess = "R"

    # Count the occurrences of each move in opponent history
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        # Check if the move is not empty before updating move_counts
        if move:
            move_counts[move] += 1

    # Find the opponent's most frequent move
    most_frequent_move = max(move_counts, key=move_counts.get)

    # Counter the opponent's most frequent move
    if most_frequent_move == "R":
        guess = "P"
    elif most_frequent_move == "P":
        guess = "S"
    elif most_frequent_move == "S":
        guess = "R"

    # Return the chosen move
    return guess
