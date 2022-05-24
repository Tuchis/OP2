"""
MODULE DOCSTRING
"""
from graph import LinkedDirectedGraph
from algorithms import dfs, breadthFirst
from linkedstack import LinkedStack


def read_file(path):
    """
    Function that reads the file and makes the graph out of the
    information in it. Returns the graph
    """
    graph = LinkedDirectedGraph()

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
            graph.addVertex(elem[0])
        # Creates edges
        for elem in lines:
            for vertex in elem[1]:
                if vertex != "none":
                    graph.addEdge(elem[0], vertex, 0)

        return graph

def bfs_test():
    """
    Function that tests the bfs with the graph. You pass the graph,
    the method tests BFS algorithm, that was realised at Stanfourd Course
    @param graph:
    @return:
    """
    graph = read_file("stanford_cs.txt")

    # TEST GRAPH
    assert(isinstance(graph, LinkedDirectedGraph))
    assert(graph.sizeVertices() == 24)
    assert(graph.sizeEdges() == 22)

    # TEST BFS
    bfs = breadthFirst(graph, "MATH51")
    assert (len(bfs) == 6)
    assert ("MATH20" in bfs)
    assert ("CS155" not in bfs)
    assert ("SC234" not in bfs)
    assert ("MATH19" == bfs[5])

    bfs = breadthFirst(graph, "CS103")
    assert (len(bfs) == 15)
    assert("MATH20" not in bfs)
    assert("MATH51" not in bfs)
    assert("CS145" in bfs)
    assert ("CS110" == bfs[11])

def dfs_test():
    """
    Function that tests the DFS with the graph. You pass the graph,
    the method tests DFS algorithm, that was realised at Stanfourd Course
    @param graph:
    @return:
    """
    graph = read_file("stanford_cs.txt")

    # TEST GRAPH
    assert(isinstance(graph, LinkedDirectedGraph))
    assert(graph.sizeVertices() == 24)
    assert(graph.sizeEdges() == 22)

    # TEST DFS
    discovered = LinkedStack()
    dfs(graph, graph.getVertex("MATH51"), discovered)
    assert(len(discovered) == 6)
    assert(graph.getVertex("MATH20") in discovered)
    assert(graph.getVertex("MATH51") in discovered)
    assert(not graph.getVertex("CS145") in discovered)
    assert (graph.getVertex("MATH51") == discovered.pop())
    assert (graph.getVertex("MATH20") != discovered.pop())

    discovered = LinkedStack()
    dfs(graph, graph.getVertex("CS103"), discovered)
    assert(len(discovered) == 15)
    assert(not graph.getVertex("MATH20") in discovered)
    assert(not graph.getVertex("MATH51") in discovered)
    assert(graph.getVertex("CS145") in discovered)
    assert (graph.getVertex("CS103") == discovered.pop())
    assert (graph.getVertex("CS145") != discovered.pop())


def main():
    """
    MAIN FUNCTION
    """
    dfs_test()
    bfs_test()


if __name__ == "__main__":
    main()
