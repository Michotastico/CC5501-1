__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from MathMethods import *

def initial_triangle(cloud):
    extremes = obtain_extremes(cloud)
    segment = first_segment(extremes)
    delete_tuple(cloud, segment)
    point = farthest_point(segment, cloud)
    triangle = (segment[0], segment[1], point)
    delete_point(cloud, point)
    return triangle
