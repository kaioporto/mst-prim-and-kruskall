class Graph(object):
    class Node(object):
        def __init__(self):
            self.neighbor = None
            self.edge = None
            self.next = None
            self.previous = None

    class Edge(object):
        def __init__(self):
            self.vertex_one, self.node_one = None, None
            self.vertex_two, self.node_two = None, None
            self.weight = 0

    def __init__(self, is_oriented=False):
        self.quantity_vertices, self.quantity_edges, self.is_oriented = None, None, is_oriented

    def get_vertices(self):
        for i in range(1, self.quantity_vertices + 1):
            yield i

    def get_edges(self, IterararSobreNo=False):
        for a_vertex in self.get_vertices():
            for w in self.get_neighbors(a_vertex, a_type="+" if self.is_oriented else "*", IterararSobreNo=IterararSobreNo):
                enumerar = True
                if not self.is_oriented:
                    wint = w if isinstance(w, int) else w.neighbor
                    enumerar = a_vertex < wint
                if enumerar:
                    yield (a_vertex, w)

    def set_quantity_vertices(self, quantity, has_previous=False):
        self.quantity_vertices, self.quantity_edges = quantity, 0
        self.nodes = [None] * (self.quantity_vertices + 1)
        for i in range(1, self.quantity_vertices + 1):
            self.nodes[i] = Graph.Node()
            self.has_previous = has_previous
        return self

    def remove_node(self, a_node):
        a_node.previous.next = a_node.next
        if a_node.next != None:
            a_node.next.previous = a_node.previous

    def remove_edge(self, an_edge):
        self.remove_node(an_edge.node_one)
        self.remove_node(an_edge.node_two)
        return self

    def add_edge(self, an_other_vertex, a_vertex, weight=0):

        an_edge = Graph.Edge()
        an_edge.vertex_one, an_edge.vertex_two, an_edge.weight = an_other_vertex, a_vertex, weight
        an_edge.node_one = self.make_node(an_other_vertex, a_vertex, an_edge, "+")
        an_edge.node_two = self.make_node(a_vertex, an_other_vertex, an_edge, "-")
        self.quantity_edges = self.quantity_edges + 1
        return self

    def is_neighbor(self, an_other_vertex, a_vertex):
        a_type = "+" if self.is_oriented else "*"
        for w in self.get_neighbors(an_other_vertex, a_type):
            if w == a_vertex:
                return True
            return False

    def get_neighbors(self, a_vertex, a_type="*", is_closed=False, use_node=False):
        if is_closed:
            a_node = Graph.Node()
            a_node.neighbor, a_node.edge, a_node.next = a_vertex, None, None
            yield a_node if use_node else a_node.neighbor
        a_next_node = self.nodes[a_vertex].next
        while a_next_node != None:
            if a_type == "*" or a_next_node.a_type == a_type:
                yield a_next_node if use_node else a_next_node.neighbor
            a_next_node = a_next_node.next

    def make_node(self, an_other_vertex, a_vertex, an_edge, a_type):
        a_node = Graph.Node()
        a_node.neighbor, a_node.edge, a_node.next, self.nodes[an_other_vertex].next = a_vertex, an_edge, self.nodes[
            an_other_vertex].next, a_node
        if self.has_previous:
            self.nodes[an_other_vertex].next.previous = self.nodes[an_other_vertex]
            if self.nodes[an_other_vertex].next.next != None:
                self.nodes[an_other_vertex].next.next.previous = self.nodes[an_other_vertex].next
        if self.is_oriented:
            a_node.a_type = a_type
        return a_node
