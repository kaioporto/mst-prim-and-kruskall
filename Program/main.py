from graph import Graph
from generator import generate_three

a_graph = Graph()

a_graph.set_quantity_vertices(5)

a_graph.add_edge(1, 2, 10)
a_graph.add_edge(1, 5, 5)
a_graph.add_edge(1, 3, 4)
a_graph.add_edge(5, 3, 2)
a_graph.add_edge(2, 3, 10)
a_graph.add_edge(2, 4, 6)

for an_edge in generate_three(a_graph):
    print("Aresta com peso %d que liga %d e %d" % (an_edge.weight, an_edge.vertex_one, an_edge.vertex_two))