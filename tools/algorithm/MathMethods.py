__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from operator import itemgetter
import math
import numpy as np

def obtain_extremes(cloud):
    x = (min(cloud, key=itemgetter(0)), max(cloud, key=itemgetter(0)))
    y = (min(cloud, key=itemgetter(1)), max(cloud, key=itemgetter(1)))
    z = (min(cloud, key=itemgetter(2)), max(cloud, key=itemgetter(2)))
    return [x, y, z]

def delete_tuple(dots, extremes):
    delete_point(dots, extremes[0])
    delete_point(dots, extremes[1])
    return

def delete_point(dots, point):
    dots.remove(point)
    return

def euclidean_distance(a, b):
    distance = math.sqrt(math.pow((a[0] - b[0]), 2) +
                         math.pow((a[1] - b[1]), 2) +
                         math.pow((a[2] - b[2]), 2))
    return distance

def first_segment(extremes):
    segment = max({euclidean_distance(extremes[0][0],extremes[0][1]): extremes[0]},
                  {euclidean_distance(extremes[1][0],extremes[1][1]): extremes[1]},
                   {euclidean_distance(extremes[2][0],extremes[2][1]): extremes[2]})
    return segment.values()[0]

def farthest_point(segment, cloud):
    m, s = get_line_vector(segment[0], segment[1])
    distance = 0
    point = None
    for p in cloud:
        d = distance_line_point(m, s, p)
        if d > distance:
            distance = d
            point = p
    return point

def get_line_vector(a, b):
    M = (a[0], a[1], a[2])
    s = (b[0]-a[0], b[1]-a[1], b[2]-a[2])
    return M, s

def distance_line_point(m, s, p):
    mm = (m[0] - p[0], m[1] - p[1], m[2] - p[2])
    dot = np.cross(np.array(mm, np.float), np.array(p, np.float))
    value = np.linalg.norm(dot)/np.linalg.norm(s)
    return value
