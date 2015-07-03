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

def initial_pyramid(cloud):
    base_triangle = initial_triangle(cloud)
    plane_triangle = calculate_triangular_plane(base_triangle[0], base_triangle[1], base_triangle[2])
    apex = farthest_point_plane(plane_triangle, cloud)
    delete_point(cloud, apex)
    pyramid = (base_triangle[0], base_triangle[1], base_triangle[2], apex)
    return pyramid
