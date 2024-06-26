from random import choice


class RandomWalk():
    def __init__(self, num_points=5000, walk_distance=list(range(0, 5))):
        self.num_points = num_points
        
        # Starting value is always 0,0
        self.x_values = [0]
        self.y_values = [0]
        self.walk_distance = walk_distance

    def fill_walk(self):
        # Keep steps until walk reaches the desired value
        while len(self.x_values) < self.num_points:
            
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next position
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    
    def get_step(self):
        # Decide which direction to go and how far to go in that direction

        direction = choice([1, -1]) # Randomly choose aif the value is positive (right) or negative (left)
        distance = choice(self.walk_distance) # Randomly choose the travel distance
        return direction * distance

