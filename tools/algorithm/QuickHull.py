__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from MathMethods import *
from tools.structures import TriangularFace, Stack, Edge


class QuickHull:

    def __init__(self, cloud):
        self.cloud = cloud
        self.stack = Stack.Stack()
        self.final_faces = list()
        return

    def initialization(self):
        self.initial_faces()
        return

    def run(self):
        self.initialization()
        while not self.stack.empty():
            self.step()
        return

    def get_faces(self):
        return self.final_faces

    def step(self):
        face = self.stack.pop()
        if not face:
            return

        if face.get_len_points() == 0:
            self.final_faces.append(face)
            return

        point = face.get_farthest_point()
        other_faces = self.stack.multi_pop(point)
        all_points = list()
        all_points.extend(face.get_points())
        for f in other_faces:
            all_points.extend(f.get_points())

        # Create new triangular faces from the edges of all visible faces to the farthest point (apex)
        new_faces = list()

        # Create a list of edges and check duplicated edges. If the edge isn't duplicated
        # Then the edge is from the borderline and we can build a triangle from this one.
        # TODO

        edges = list()

        edges.append(Edge.Edge(face.a(), face.b()))
        edges.append(Edge.Edge(face.b(), face.c()))
        edges.append(Edge.Edge(face.c(), face.a()))

        # Add new edges from every face.
        for f in other_faces:
            # Create edges
            edge1 = Edge.Edge(f.a(), f.b())
            edge2 = Edge.Edge(f.b(), f.c())
            edge3 = Edge.Edge(f.c(), f.a())
            # Set boolean for duplicated edges
            bool1 = False
            bool2 = False
            bool3 = False
            # List for elements duplicated
            delete_list = list()

            # Check for every appended edge.
            for e in edges:
                # If the edge is equals to one of the news, check the boolean and append to delete list
                if e.is_equals(edge1):
                    bool1 = True
                    delete_list.append(e)
                if e.is_equals(edge2):
                    bool2 = True
                    delete_list.append(e)
                if e.is_equals(edge3):
                    bool3 = True
                    delete_list.append(e)
            # Remove internal edges
            for d in delete_list:
                edges.remove(d)
            # Add external edges
            if not bool1:
                edges.append(edge1)
            if not bool2:
                edges.append(edge2)
            if not bool3:
                edges.append(edge3)

        # Now we have the borderline.

        for edge in edges:
            triangle = TriangularFace.TriangularFace(edge.a(), edge.b(), point)
            new_faces.append(triangle)

        # Assign points to faces
        for p in all_points:
            for f in new_faces:
                f.add_point(p)

        # Push the new faces to the stack
        for f in new_faces:
            self.stack.push(f)
        return

    def initial_triangle(self):
        extremes = obtain_extremes(self.cloud)
        segment = first_segment(extremes)
        delete_tuple(self.cloud, segment)
        point = farthest_point(segment, self.cloud)
        triangle = (segment[0], segment[1], point)
        delete_point(self.cloud, point)
        return triangle

    def initial_pyramid(self):
        base_triangle = self.initial_triangle()
        plane_triangle = calculate_triangular_plane(base_triangle[0], base_triangle[1], base_triangle[2])
        apex = farthest_point_plane(plane_triangle, self.cloud)
        delete_point(self.cloud, apex)
        pyramid = (base_triangle[0], base_triangle[1], base_triangle[2], apex)
        return pyramid

    def initial_faces(self):
        pyramid = self.initial_pyramid()
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

        for p in self.cloud:
            for f in faces:
                f.add_point(p)

        for f in faces:
            self.stack.push(f)
        return
