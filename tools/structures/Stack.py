__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
class Stack:

    def __init__(self):
        self.stack = list()
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
        return all_points

    def __str__(self):
        string = "Stack:\n"
        for f in self.stack:
            string = string + str(f) + "\n"

        string = string + "End Stack\n"

        return string
