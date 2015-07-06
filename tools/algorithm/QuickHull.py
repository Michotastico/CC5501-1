__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from MathMethods import *
from tools.structures import TriangularFace, Stack
class QuickHull:

    def __init__(self, cloud):
        self.cloud = cloud
        self.stack = Stack.Stack()
        return

    def initial_triangle(self, cloud):
        extremes = obtain_extremes(cloud)
        segment = first_segment(extremes)
        delete_tuple(cloud, segment)
        point = farthest_point(segment, cloud)
        triangle = (segment[0], segment[1], point)
        delete_point(cloud, point)
        return triangle

    def initial_pyramid(self, cloud):
        base_triangle = self.initial_triangle(cloud)
        plane_triangle = calculate_triangular_plane(base_triangle[0], base_triangle[1], base_triangle[2])
        apex = farthest_point_plane(plane_triangle, cloud)
        delete_point(cloud, apex)
        pyramid = (base_triangle[0], base_triangle[1], base_triangle[2], apex)
        return pyramid

    def initial_faces(self, cloud):
        pyramid = self.initial_pyramid(cloud)
        faces = list()

        # Check Normals

        face_1 = TriangularFace.TriangularFace(pyramid[0], pyramid[1], pyramid[2])
        if face_1.distance(pyramid[3]) > 0:
            face_1.invert_normal()
        faces.append(face_1)
        face_2 = TriangularFace.TriangularFace(pyramid[0], pyramid[1], pyramid[3])
        if face_2.distance(pyramid[2]) > 0:
            face_2.invert_normal()
        faces.append(face_2)
        face_3 = TriangularFace.TriangularFace(pyramid[1], pyramid[2], pyramid[3])
        if face_3.distance(pyramid[0]) > 0:
            face_3.invert_normal()
        faces.append(face_3)
        face_4 = TriangularFace.TriangularFace(pyramid[0], pyramid[2], pyramid[3])
        if face_4.distance(pyramid[1]) > 0:
            face_4.invert_normal()
        faces.append(face_4)

        # Set points to faces

        for p in cloud:
            for f in faces:
                f.add_point(p)

        for f in faces:
            self.stack.push(f)

        return


