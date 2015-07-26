__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"


class Edge:

    def __init__(self, vertex_a, vertex_b):
        self.va = vertex_a
        self.vb = vertex_b

    def is_equals(self, other_edge):
        boolean_va1 = self.va[0] == other_edge.va[0] & self.va[1] == other_edge.va[1] & self.va[2] == other_edge.va[2]
        boolean_va2 = self.va[0] == other_edge.vb[0] & self.va[1] == other_edge.vb[1] & self.va[2] == other_edge.vb[2]

        boolean_vb1 = self.vb[0] == other_edge.va[0] & self.vb[1] == other_edge.va[1] & self.vb[2] == other_edge.va[2]
        boolean_vb2 = self.vb[0] == other_edge.vb[0] & self.vb[1] == other_edge.vb[1] & self.vb[2] == other_edge.vb[2]

        boolean_va = boolean_va1 | boolean_va2
        boolean_vb = boolean_vb1 | boolean_vb2

        return boolean_va & boolean_vb

    def a(self):
        return self.va

    def b(self):
        return self.vb
