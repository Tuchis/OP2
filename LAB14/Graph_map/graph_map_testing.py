"""
MODULE DOCSTRING
"""
from graph import Graph
from dfs import DFS, construct_path
from bfs import BFS
from topological_sort import topological_sort


def read_file(path, directed = False):
    """
    Function that reads the file and makes the graph out of the
    information in it. Returns the graph
    """
    graph = Graph(directed)

    with open(path) as file:
        lines = []
        # Reads lines and saves vertexes into the list
        for line in file:
            if not line.startswith("#"):
                for unwanted_sign in [",", "(", ")"]:
                    line = line.replace(unwanted_sign, " ")
                lines.append((line.strip().split()[0],
                              line.strip().split()[1:]))
        # Creates vertexes
        for elem in lines:
            graph.insert_vertex(elem[0])
        # Creates edges
        for elem in lines:
            for vertex in graph.vertices():
                if vertex.element() == elem[0]:
                    start_vertex = vertex
            for vert in elem[1]:
                if vert != "none":
                    for vertex in graph.vertices():
                        if vertex.element() == vert:
                            end_vertex = vertex
                    graph.insert_edge(start_vertex, end_vertex)

        return graph

def get_vertix(graph, value):
    for vertex in list(graph.vertices()):
        if vertex.element() == value:
            return vertex

def bfs_test():
    """
    Function that tests the bfs with the graph.
    The method tests BFS algorithm, that was realised at Stanfourd Course
    @param graph:
    @return:
    """
    graph = read_file("stanford_cs.txt")
    # TEST GRAPH
    assert(isinstance(graph, Graph))
    assert(not graph.is_directed())
    assert(graph.edge_count() == 22)
    assert(graph.vertex_count() == 24)

    # TEST BFS
    discovered = {}
    BFS(graph, get_vertix(graph, "MATH19"), discovered)
    assert (len(discovered) == 6)
    assert (get_vertix(graph, "MATH20") in discovered)
    assert (get_vertix(graph, "CS155") not in discovered)
    assert (get_vertix(graph, "CS106B") not in discovered)
    assert (get_vertix(graph, "MATH19") == list(discovered.keys())[1])

    discovered = {}
    BFS(graph, get_vertix(graph, "CS103"), discovered)
    assert(len(discovered) == 15)
    assert(not get_vertix(graph, "MATH20") in discovered)
    assert(not get_vertix(graph, "MATH51") in discovered)
    assert(get_vertix(graph, "CS145") in discovered)
    assert(get_vertix(graph, "CS106B") == list(discovered.keys())[6])

def dfs_test():
    """
    Function that tests the DFS with the graph.
    The method tests DFS algorithm, that was realised at Stanfourd Course
    @param graph:
    @return:
    """
    graph = read_file("stanford_cs.txt")

    # TEST GRAPH
    assert(isinstance(graph, Graph))
    assert(not graph.is_directed())
    assert(graph.edge_count() == 22)
    assert(graph.vertex_count() == 24)

    # TEST DFS
    discovered = {}
    DFS(graph, get_vertix(graph, "MATH51"), discovered)
    assert(len(discovered) == 6)
    assert(get_vertix(graph, "MATH20") in discovered)
    assert(get_vertix(graph, "MATH51") in discovered)
    assert(not get_vertix(graph, "CS145") in discovered)
    assert(len(construct_path(get_vertix(graph, "MATH51"),
            get_vertix(graph, "MATH20"), discovered)) == 3)
    assert (get_vertix(graph, "MATH19") == list(discovered.keys())[2])

    discovered = {}
    DFS(graph, get_vertix(graph, "CS103"), discovered)
    assert(len(discovered) == 15)
    assert(not get_vertix(graph, "MATH20") in discovered)
    assert(not get_vertix(graph, "MATH51") in discovered)
    assert(get_vertix(graph, "CS145") in discovered)
    assert (get_vertix(graph, "CS106B") == list(discovered.keys())[7])


def topological_sort_test():
    """
    Function to test topological sort realised by Stanford Course
    The method tests graph and topological sort in it.
    """
    graph = read_file("stanford_cs.txt", True)

    # TEST GRAPH
    assert(isinstance(graph, Graph))
    assert(graph.is_directed())
    assert(graph.edge_count() == 22)
    assert(graph.vertex_count() == 24)

    # TEST TOPOLOGICAL SORT
    topo = topological_sort(graph)
    assert(get_vertix(graph, "MATH20") in topo)
    assert(get_vertix(graph, "CS145") in topo)
    assert(get_vertix(graph, "ENGR40M") in topo)
    assert(get_vertix(graph, "CS107") == topo[15])

def main():
    """
    MAIN FUNCTION
    """
    # bfs_test()
    dfs_test()
    bfs_test()
    topological_sort_test()


if __name__ == "__main__":
    main()
