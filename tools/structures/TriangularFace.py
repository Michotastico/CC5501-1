__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from tools.algorithm import MathMethods

class TriangularFace:

    def __init__(self, va, vb, vc):
        self.vertexA = va
        self.vertexB = vb
        self.vertexC = vc
        self.plane = MathMethods.calculate_triangular_plane(va, vb, vc)
        self.points = list()
        return

    def add_point(self, point):
        distance = MathMethods.point_plane_distance_no_abs(point, self.plane)
        if distance > 0:
            self.points.append(point)
        return

    def invert_normal(self):
        self.plane = MathMethods.calculate_triangular_plane(self.vertexC, self.vertexB, self.vertexA)
        return

    def __contains__(self, point):
        for p in self.points:
            if p[0] == point[0]:
                if p[1] == point[1]:
                    if p[2] == point[2]:
                        return True
        return False

