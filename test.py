
def bfs(graph, s, end):

    visited = {s: 0}
    parent = {s: None}

    frontier=[s]
    l=0
    while end not in visited:
    
        l+=1
        new_frontier = []
        for u in frontier:
            for v in graph[u]:
                if v not in visited:
                    visited[v] = l
                    parent[v] = u
                    new_frontier.append(v)
        frontier = new_frontier
    
    
    path = []
    p = end
    while p is not None:
        path.append(p)
        p = parent[p]
    
    path.reverse()
    return path


print(bfs([[1, 2], [3], [1], []], 0, 3))