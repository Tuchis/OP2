"""
MODULE DOCSTRING
"""
from graph import LinkedDirectedGraph
from algorithms import dfs, breadthFirst, topoSort
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
    assert (len(bfs) == 4)
    assert ("MATH20" in bfs)
    assert ("CS155" not in bfs)
    assert ("SC234" not in bfs)
    assert ("MATH19" == bfs[3])

    bfs = breadthFirst(graph, "CS103")
    assert (len(bfs) == 2)
    assert("MATH20" not in bfs)
    assert("MATH51" not in bfs)
    assert ("CS103" == bfs[0])

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
    assert(len(discovered) == 4)
    assert(graph.getVertex("MATH20") in discovered)
    assert(graph.getVertex("MATH51") in discovered)
    assert(not graph.getVertex("CS145") in discovered)
    assert (graph.getVertex("MATH51") == discovered.pop())
    assert (graph.getVertex("MATH20") != discovered.pop())

    discovered = LinkedStack()
    dfs(graph, graph.getVertex("CS103"), discovered)
    assert(len(discovered) == 2)
    assert(not graph.getVertex("MATH20") in discovered)
    assert(not graph.getVertex("MATH51") in discovered)
    assert(graph.getVertex("CS145") not in discovered)
    assert (graph.getVertex("CS103") == discovered.pop())
    assert (graph.getVertex("CS145") != discovered.pop())

def topological_sort_test():
    """
    Function to test topological sort in directed graph
    """
    graph = read_file("stanford_cs.txt")

    # TEST GRAPH
    assert(isinstance(graph, LinkedDirectedGraph))
    assert(graph.sizeVertices() == 24)
    assert(graph.sizeEdges() == 22)

    # TEST TOPOLOGICAL SORT
    topological_sort = topoSort(graph, graph.getVertex("MATH20"))
    assert(len(topological_sort) == 24)
    assert(topological_sort.pop() == graph.getVertex("MATH53"))
    assert(topological_sort.pop() != graph.getVertex("MATH20"))
    assert(topological_sort.pop())
    assert(len(topological_sort) == 21)


def main():
    """
    MAIN FUNCTION
    """
    timer = time.time()
    print("Start of the tests...")
    print("DSF TESTS...")
    dfs_test()
    print("BFS TESTS...")
    bfs_test()
    print("TOPOLOGICAL SORT TESTS...")
    topological_sort_test()
    print("ALL TESTS PASSED. CONGRATULATIONS")
    print("Time of the tests: ", time.time() - timer, "seconds")


if __name__ == "__main__":
    import time
    main()
