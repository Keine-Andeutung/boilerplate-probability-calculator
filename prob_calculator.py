import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **colored_balls) -> None:
        self.contents = []
        for (key, value) in colored_balls.items():
            self.contents.extend([key]*value)

    def draw(self, number_of_balls: int):
        if number_of_balls >= len(self.contents):
            balls_drawn = self.contents.copy()
            self.contents.clear()
            return balls_drawn
        else:
            balls_drawn = []
            for i in range(number_of_balls):
                balls_drawn.append(self.contents.pop(random.randrange(len(self.contents))))
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_succesful_experiments=0.0
    for exp in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        expected_balls_copy=copy.copy(expected_balls)
        for (key, value) in expected_balls.items():
            for i in range(value):
                if key in drawn_balls:
                    drawn_balls.remove(key)
                    expected_balls_copy[key] -= 1
                    if expected_balls_copy[key] == 0:
                        expected_balls_copy.pop(key)
                        break
        if expected_balls_copy == {}:
            num_succesful_experiments += 1
    return num_succesful_experiments / num_experiments


