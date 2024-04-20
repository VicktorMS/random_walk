import matplotlib.pyplot as plt

from random_walk import RandomWalk



colors = ['red', 'blue', 'yellow', 'green']

for color in colors:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, c=color, s=15)

plt.show()