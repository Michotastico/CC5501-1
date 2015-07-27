__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"


class Edge:

    def __init__(self, vertex_a, vertex_b):
        self.va = vertex_a
        self.vb = vertex_b

    def is_equals(self, other_edge):
        boolean_va11 = self.va[0] == other_edge.va[0]
        boolean_va12 = self.va[1] == other_edge.va[1]
        boolean_va13 = self.va[2] == other_edge.va[2]
        boolean_va1 = boolean_va11 & boolean_va12 & boolean_va13

        boolean_va21 = self.va[0] == other_edge.vb[0]
        boolean_va22 = self.va[1] == other_edge.vb[1]
        boolean_va23 = self.va[2] == other_edge.vb[2]
        boolean_va2 = boolean_va21 & boolean_va22 & boolean_va23

        boolean_vb11 = self.vb[0] == other_edge.va[0]
        boolean_vb12 = self.vb[1] == other_edge.va[1]
        boolean_vb13 = self.vb[2] == other_edge.va[2]
        boolean_vb1 = boolean_vb11 & boolean_vb12 & boolean_vb13

        boolean_vb21 = self.vb[0] == other_edge.vb[0]
        boolean_vb22 = self.vb[1] == other_edge.vb[1]
        boolean_vb23 = self.vb[2] == other_edge.vb[2]
        boolean_vb2 = boolean_vb21 & boolean_vb22 & boolean_vb23

        boolean_va = boolean_va1 | boolean_va2
        boolean_vb = boolean_vb1 | boolean_vb2

        return boolean_va & boolean_vb

    def a(self):
        return self.va

    def b(self):
        return self.vb
