from disjoint import Disjoint
from graph import Graph
def kruskal_generator(a_graph: Graph):
    an_union = Disjoint(a_graph.quantity_vertices)
    for a_vertex in a_graph.get_vertices():
        an_union.insert_vertex(a_vertex)

    an_edges_three = []
    a_edges_list = []

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

def prim_generator(a_graph: Graph, a_root_vertex = 1):
    an_union = Disjoint(a_graph.quantity_vertices)
    for a_vertex in a_graph.get_vertices():
        an_union.insert_vertex(a_vertex)

    an_edges_three = []
    an_edges_list = []
    a_vertex_list = [a_root_vertex]

    while len(a_vertex_list) < a_graph.quantity_vertices:
        for a_node in a_graph.get_neighbors(a_vertex_list[-1], use_node=True):
            if an_union.get_group(a_vertex_list[-1]) != an_union.get_group(a_node.neighbor):
                an_edges_list.append(a_node.edge)

        an_edges_list.sort(key=lambda an_edge: an_edge.weight)

        for a_edge in an_edges_list:
            if an_union.get_group(a_edge.vertex_two) != an_union.get_group(a_edge.vertex_one):
                an_union.join(a_edge.vertex_one, a_edge.vertex_two)
                an_edges_three.append(a_edge)
                a_vertex_list.append(a_edge.vertex_one if a_edge.vertex_one not in a_vertex_list else a_edge.vertex_two)
                break

    return an_edges_three
