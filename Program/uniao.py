class Disjoint:
    def __init__(self, quantity):
        self.Pai, self.n = [None] * (quantity + 1), 0

    def join(self, a_vertex, an_other_vertex):
        Ru = self.get_group(a_vertex)
        Rv = self.get_group(an_other_vertex)

        if Ru != Rv:
            if -self.Pai[Ru] < -self.Pai[Rv]:
                self.Pai[Ru], self.Pai[Rv] = Rv, self.Pai[Rv] + self.Pai[Ru]
            else:
                self.Pai[Rv], self.Pai[Ru] = Ru, self.Pai[Rv] + self.Pai[Ru]

    def get_group(self, a_vertex):
        if self.Pai[a_vertex] > 0:
            self.Pai[a_vertex] = self.Conjunto(self.Pai[a_vertex])
            return self.Pai[a_vertex]
        else:
            return a_vertex

    def insert_vertex(self, a_vertex):
        self.Pai[self.n + 1], self.n = -1, self.n + 1