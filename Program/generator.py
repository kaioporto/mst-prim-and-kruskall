from disjoint import Disjoint
from graph import Graph
def generate_three(a_graph: Graph):
    an_union = Disjoint(a_graph.quantity_vertices)
    for a_vertex in a_graph.get_vertices():
        an_union.insert_vertex(a_vertex)

    an_edges_three = []; a_edges_list = []

    for a_vertex in a_graph.get_vertices():
        for a_node in a_graph.get_neighbors(a_vertex, use_node=True):
            if a_node.neighbor < a_vertex:
                a_edges_list.append(a_node.edge)

    a_edges_list.sort(key=lambda an_edge: an_edge.weight)

    for a_edge in a_edges_list:
        a_vertex, an_other_vertex = a_edge.vertex_one, a_edge.vertex_two
        if an_union.get_group(a_vertex) != an_union.get_group(an_other_vertex):
            an_union.join(a_vertex, an_other_vertex)
            an_edges_three.append(a_edge)
    return an_edges_three