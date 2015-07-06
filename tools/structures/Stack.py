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
        if len(self.stack) != 0:
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

