from collections import deque
def bfs(a,node):
    nq=deque([node])
    v=set()
    v.add(node)
    while nq:
        n=nq.popleft()
        print(n)
        for nb in a[n]:
            if nb not in v:
                nq.append(nb)
                v.add(nb)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G','H'],
    'G':[],
    'H':[]
}

print("BFS Traversal:")
bfs(graph, 'A')
                
