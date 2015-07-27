__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
import QuickHull

class Layers:

    def __init__(self, cloud):
        self.cloud = cloud
        self.layers = list()

    def run(self):
        while len(self.cloud) >= 4:
            points = list()
            for p in self.cloud:
                points.append(p)

            algorithm = QuickHull.QuickHull(points)
            algorithm.run()
            faces = algorithm.get_faces()
            self.layers.append(faces)
            for f in faces:
                if self.cloud.index(f.a()) >= 0:
                    self.cloud.remove(f.a())
                if self.cloud.index(f.b()) >= 0:
                    self.cloud.remove(f.b())
                if self.cloud.index(f.c()) >= 0:
                    self.cloud.remove(f.c())

    def get_layers(self):
        return self.layers