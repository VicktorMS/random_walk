import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(num_points=5000, walk_distance=list(range(0, 5)))
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 6))
    
    plt.scatter(rw.x_values, rw.y_values, c="red", s=1)
    #plt.plot(rw.x_values, rw.y_values, color='red', linewidth=1)

    plt.show()

    keep_running = input('Create another walk? (Y/N)')
    if keep_running.lower() != 'y': break