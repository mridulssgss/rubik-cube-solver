import rubik


def update_frontier(visited1, visited2, parent, frontier, l):
    """update the information based on new frontier"""
    new_frontier = [] 
    for state in frontier:
        for perm in rubik.quarter_twists:
            s = rubik.perm_apply(perm, state)
            if s not in visited1:
                visited1[s]=l
                parent[s]=perm
                new_frontier.append(s)
                if s in visited2:
                    return (s, new_frontier)
    
    return (None, new_frontier)


def return_path(parent1, parent2, vertex):
    """for a given vertex construct an path"""
    
    path1 = []
    path2 = []
    
    p1 = parent1[vertex]
    v1 = vertex
    while p1 is not None:
        path1.append(p1)
        v1 = rubik.perm_apply(rubik.perm_inverse(p1), v1)
        p1 = parent1[v1]
    
    p2 = parent2[vertex]
    v2 = vertex
    while p2 is not None:
        path2.append(rubik.perm_inverse(p2))
        v2 = rubik.perm_apply(rubik.perm_inverse(p2), v2)
        print(v2)
        p2 = parent2[v2]

    path1.reverse()
    return path1 + path2



def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if(start == end): return []
    visited1 = {start: 0} #frontier for first bfs along with level
    visited2 = {end: 0} #frontier for second bfs along with level

    parent1 = {start: None} #keeps the parent pointer of first bfs moves
    parent2 = {end: None} #keeps the parent pointer of second bfs's moves

    frontier1 = [start] #frontier for first bfs
    frontier2 = [end] #frontier for second bfs


    l = 0 #keeps the left level counter
    r = 0 #keeps the right level counter
    mid_vertex = None
    while mid_vertex is None and l < 8:
        l +=1
        r +=1
        mid_vertex , frontier1=update_frontier(visited1, visited2, parent1, frontier1, l)
        if mid_vertex is None:
            mid_vertex, frontier2=update_frontier(visited2, visited1, parent2, frontier2, r)

            
    return return_path(parent1, parent2, mid_vertex) if l < 8 else None
    
