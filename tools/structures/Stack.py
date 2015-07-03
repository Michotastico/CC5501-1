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
        return self.stack.pop()

    def multi_pop(self, point):
        faces = list()
        for face in self.stack:
            if point in face:
                faces.append(face)
        for face in faces:
            self.stack.remove(face)

        return faces

