__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
class Stack:

    def __init__(self, delta):
        self.stack = list()
        self.DELTA = delta
        return

    def push(self, face):
        self.stack.append(face)
        return

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return False

    def multi_pop(self, point):
        faces = list()
        for face in self.stack:
            if point in face:
                faces.append(face)
        for face in faces:
            self.stack.remove(face)

        return faces

    def empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def get_all_points(self):
        all_points = list()
        for face in self.stack:
            all_points.extend(face.get_points())
        return self.delete_duplicated_points(all_points)

    def delete_duplicated_points(self, points):
        final_points = list()
        while len(points) != 0:
            p = points.pop()
            to_delete = list()
            duplicated = False
            for pp in points:
                if (p[0] <= pp[0]+self.DELTA) & (p[0] >= pp[0]-self.DELTA):
                    if (p[1] <= pp[1]+self.DELTA) & (p[1] >= pp[1]-self.DELTA):
                        if (p[2] <= pp[2]+self.DELTA) & (p[1] >= pp[1]-self.DELTA):
                            duplicated = True
                            to_delete.append(pp)
            final_points.append(p)
            if duplicated:
                for ptd in to_delete:
                    if points.index(ptd) >= 0:
                        points.remove(ptd)
        return final_points

    def __str__(self):
        string = "Stack:\n"
        for f in self.stack:
            string = string + str(f) + "\n"

        string = string + "End Stack\n"

        return string

    def size(self):
        return len(self.stack)
