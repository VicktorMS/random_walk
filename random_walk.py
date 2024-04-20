from random import choice


class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Starting value is always 0,0
        self.x_values = [0]
        self.y_values = [0]
        self.walk_dis = 0 

    def fill_walk(self):
        # Keep steps until walk reaches the desired value
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how far to go in that direction

            x_direction = choice([1, -1]) # Randomly choose aif the value is positive (right) or negative (left)
            x_distance = choice([0, 1, 2, 3, 4]) # Randomly choose the travel distance
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1]) 
            y_distance = choice([0, 1, 2, 3, 4]) 
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next position
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

            