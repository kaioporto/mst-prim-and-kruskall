class Graph(object):
    class Node(object):
        def __init__(self):
            self.neighbor = None
            self.edge = None
            self.next = None

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
        for v in self.get_vertices():
            for w in self.get_neighbors(v, Tipo="+" if self.is_oriented else "*", IterararSobreNo=IterararSobreNo):
                enumerar = True
                if not self.is_oriented:
                    wint = w if isinstance(w, int) else w.neighbor
                    enumerar = v < wint
                if enumerar:
                    yield (v, w)

    def set_quantity_vertices(self, quantity, has_before_node=False):
        self.quantity_vertices, self.quantity_edges = quantity, 0
        self.nodes = [None] * (self.quantity_vertices + 1)
        for i in range(1, self.quantity_vertices + 1):
            self.nodes[i] = Graph.Node()
            self.has_before_node = has_before_node
        return self

    def RemoverAresta(self, uv):
        """
        Remove a aresta uv
        """

        def RemoverLista(a_node):
            a_node.Ant.next = a_node.next
            if a_node.next != None:
                a_node.next.Ant = a_node.Ant

        RemoverLista(uv.node_one)
        RemoverLista(uv.node_two)

    def add_edge(self, u, v, weight=0):

        an_edge = Graph.Edge()
        an_edge.vertex_one, an_edge.vertex_two, an_edge.weight = u, v, weight
        an_edge.node_one = self.make_node(u, v, an_edge, "+")
        an_edge.node_two = self.make_node(v, u, an_edge, "-")
        self.quantity_edges = self.quantity_edges + 1
        return self

    def is_neighbor(self, u, v):
        Tipo = "+" if self.is_oriented else "*"
        for w in self.get_neighbors(u, Tipo):
            if w == v:
                return True
            return False

    def get_neighbors(self, v, Tipo="*", Fechada=False, use_node=False):
        if Fechada:
            a_node = Graph.Node()
            a_node.neighbor, a_node.edge, a_node.next = v, None, None
            yield a_node if use_node else a_node.neighbor
        w = self.nodes[v].next
        while w != None:
            if Tipo == "*" or w.Tipo == Tipo:
                yield w if use_node else w.neighbor
            w = w.next

    def make_node(self, an_other_vertex, a_vertex, an_edge, Tipo):
        a_node = Graph.Node()
        a_node.neighbor, a_node.edge, a_node.next, self.nodes[an_other_vertex].next = a_vertex, an_edge, self.nodes[
            an_other_vertex].next, a_node
        if self.has_before_node:
            self.nodes[an_other_vertex].next.Ant = self.nodes[an_other_vertex]
            if self.nodes[an_other_vertex].next.next != None:
                self.nodes[an_other_vertex].next.next.Ant = self.nodes[an_other_vertex].next
        if self.is_oriented:
            a_node.Tipo = Tipo
        return a_node
