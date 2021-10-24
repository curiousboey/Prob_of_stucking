import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import product, combinations

length_of_cube = 10
start = [0,0]
div_len=length_of_cube/2

plt.plot([-div_len,div_len,div_len,div_len,div_len,-div_len,-div_len,-div_len],[-div_len,-div_len,-div_len,div_len,div_len,div_len,div_len,-div_len],color='red', linestyle='solid', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)


random_walk = ([-1,0],[0,1],[1,0],[-1,-1])
points = []
points.append(start)

while random_walk != []:
    random_walk = ([-1, 0], [0, 1], [1, 0], [0, -1])
    r = random_walk[int(np.random.randint(0,4,1))]
    new_point = [a + b for a, b in zip(points[len(points)-1], r)] #element wise additions
    j=0
    for i in range(len(points)):
        if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
            j += 1
        else:
            pass

    if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
        points.append(new_point)
    else:
        random_walk = list(random_walk)
        random_walk.remove(r)
        random_walk = tuple(random_walk)
        r = random_walk[int(np.random.randint(0, 3, 1))]
        new_point = [a + b for a, b in zip(points[len(points) - 1], r)]  # element wise additions
        j=0
        for i in range(len(points)):
            if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                j += 1
            else:
                pass
        if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
            points.append(new_point)
        else:
            random_walk = list(random_walk)
            random_walk.remove(r)
            random_walk = tuple(random_walk)
            r = random_walk[int(np.random.randint(0, 2, 1))]
            new_point = [a + b for a, b in zip(points[len(points) - 1], r)]  # element wise additions
            j = 0
            for i in range(len(points)):
                if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                    j += 1
                else:
                    pass
            if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                points.append(new_point)
            else:
                random_walk = list(random_walk)
                random_walk.remove(r)
                random_walk = tuple(random_walk)
                r = random_walk[int(np.random.randint(0, 1, 1))]
                new_point = [a + b for a, b in zip(points[len(points) - 1], r)]  # element wise additions
                j = 0
                for i in range(len(points)):
                    if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                        j += 1
                    else:
                        pass
                if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                    points.append(new_point)
                else:
                    random_walk = []

x_points = []
y_points = []
for q in range(len(points)):
    x_points.append(points[q][0])
    y_points.append(points[q][1])

plt.plot(x_points, y_points,color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=4)
finish = points[len(points)-1]
plt.text(x=0, y=0, s="start")
plt.text(x=finish[0], y=finish[1], s="finish")
plt.grid()
plt.show()






