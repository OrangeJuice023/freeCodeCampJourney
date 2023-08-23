import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            for _ in range(num_balls):
                random_index = random.randint(0, len(self.contents) - 1)
                drawn_ball = self.contents.pop(random_index)
                drawn_balls.append(drawn_ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

        success = True
        for ball, count in expected_balls.items():
            if ball not in drawn_balls_dict or drawn_balls_dict[ball] < count:
                success = False
                break
        
        if success:
            num_successful += 1

    probability = num_successful / num_experiments
    return probability
