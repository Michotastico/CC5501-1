__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from random import uniform, randint, choice

def make_point(min, max):
    a = randint(min, max)
    b = randint(min, max)
    while b == a:
        b = randint(min, max)
    c = randint(min, max)
    while (c == a) | (c == b):
        c = randint(min, max)
    point = (a, b, c)

    return point

def make_points(min, max, number):
    points = list()
    i = 0
    while i < number :
        p = make_point(min, max)
        points.append(p)
        i +=1
    return points

def random_color():
    c1 = (0.0, 0.1, 0.2)
    c2 = (0.1, 0.2, 0.3)
    c3 = (0.2, 0.3, 0.4)
    c4 = (0.4, 0.5, 0.6)
    colors = [c1, c2, c3, c4]
    return choice(colors)

