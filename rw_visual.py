import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, c='red', s=15)
    plt.show()

    keep_running = input('Create another walk? (Y/N)')
    if keep_running.lower() != 'y': break