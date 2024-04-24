import pygal

from random_walk import RandomWalk

while True:
    rw = RandomWalk(num_points=5000, walk_distance=list(range(0, 5)))
    rw.fill_walk()

    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = f'Random Walk With {rw.num_points}'

    xy_values = []

    for index, x_value in enumerate(rw.x_values):
        xy_values.append((x_value, rw.y_values[index]))

    xy_chart.add(str(rw.num_points), xy_values)
    xy_chart.render_to_file('random_walk.svg')


    keep_running = input('Create another walk? (Y/N)')
    if keep_running.lower() != 'y': break