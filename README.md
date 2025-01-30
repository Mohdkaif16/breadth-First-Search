# breadth-First-Search
search method
Pseudocode:

    BFS(graph, start_node):
    Create an empty queue Q
    Create a set visited to keep track of visited nodes 
    Enqueue start_node into Q
    Mark start_node as visited
    while Q is not empty:
        node = Dequeue from Q
        Process node  (print or store)
        for each neighbor in graph[node]:
            if neighbor is not in visited:
                Enqueue neighbor into Q
                Mark neighbor as visited
    graph="data set or tree structure"
    start_node="starting node or point for search"
    BFS(graph,start_node)

