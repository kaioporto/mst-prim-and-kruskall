class Disjoint:
    def __init__(self, quantity):
        self.groups, self.n = [None] * (quantity + 1), 0

    def get_quantity(self, a_vertex):
        if self.has_quantity(a_vertex):
            return -self.groups[a_vertex]
        else:
            return self.get_quantity(self.get_group(a_vertex))

    def update_group(self, a_vertex):
        self.groups[a_vertex] = self.get_group(self.groups[a_vertex])
        return self.groups[a_vertex]

    def get_group(self, a_vertex):
        if not self.has_quantity(a_vertex):
            return self.update_group(a_vertex)
        else:
            return a_vertex

    def has_quantity(self, a_vertex):
        return self.groups[a_vertex] < 0

    def insert_vertex(self, a_vertex):
        self.groups[self.n + 1], self.n = -1, self.n + 1
        return self

    def join(self, a_vertex, an_other_vertex):
        if self.get_group(a_vertex) != self.get_group(an_other_vertex):
            if self.get_quantity(a_vertex) < self.get_quantity(an_other_vertex):
                self.groups[self.get_group(a_vertex)], self.groups[self.get_group(an_other_vertex)] = self.get_group(
                    an_other_vertex), -(self.get_quantity(an_other_vertex) + self.get_quantity(a_vertex))
            else:
                self.groups[self.get_group(an_other_vertex)], self.groups[self.get_group(a_vertex)] = self.get_group(
                    a_vertex), -(self.get_quantity(an_other_vertex) + self.get_quantity(a_vertex))
        return self
