from pylab import *
import matplotlib.pyplot as plt

import math

def bezier_curve (time = [], point_a = [], point_b = [], point_c = []):
    x = []
    y = []

    for dt in time:
        # line from point a to point b
        x1 = point_a[0] + (point_b[0] - point_a[0]) * dt
        y1 = point_a[1] + (point_b[1] - point_a[1]) * dt

        # line from point b to point c
        x2 = point_b[0] + (point_c[0] - point_b[0]) * dt
        y2 = point_b[1] + (point_c[1] - point_b[1]) * dt

        # combination of the two lines
        x.append(x1 + (x2 - x1) * dt)
        y.append(y1 + (y2 - y1) * dt)

    return {'x':x, 'y':y}



x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []

# get handle to figure
fig = plt.figure()
ax = fig.add_subplot (111)

time = arange(0, 1, 0.01)

# First set of points
start_point = [0.0,0.0]
mid_point   = [8.0,3.0]
end_point   = [10.0,0.0]

# all lines will share start and end points
plt.plot(start_point[0], start_point[1], 'b.')
plt.plot(end_point[0], end_point[1], 'b.')

result = bezier_curve (time, start_point, mid_point, end_point)
x1 = result['x']
y1 = result['y']

#plot results
plt.plot(mid_point[0], mid_point[1], 'r.')
plt.plot(x1, y1, 'r-')

# Second set of points
start_point = [0.0,0.0]
mid_point   = [2.0,3.0]
end_point   = [10.0,0.0]

result = bezier_curve (time, start_point, mid_point, end_point)
x2 = result['x']
y2 = result['y']

plt.plot(mid_point[0], mid_point[1], 'g.')
plt.plot(x2, y2, 'g-')

# Third set of points
start_point = [0.0,0.0]
mid_point   = [7.0,5.0]
end_point   = [10.0,0.0]

result = bezier_curve (time, start_point, mid_point, end_point)
x3 = result['x']
y3 = result['y']

plt.plot(mid_point[0], mid_point[1], 'k.')
plt.plot(x3, y3, 'k-')

# set the axis limits and square aspect ratio
ax.axis([-1, 11, -1, 6])
ax.set_aspect('equal')

show()
