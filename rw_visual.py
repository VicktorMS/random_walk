import matplotlib.pyplot as plt

from random_walk import RandomWalk



colors = ['inferno', 'cool', 'magma', 'viridis']

for color in colors:
    rw = RandomWalk()
    point_numbers = list(range(rw.num_points))
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=color, s=15)

plt.show()