import rubik


def update_frontier(visited1, visited2, parent, frontier, l):
    """update the information based on new frontier"""
    flag = False
    new_frontier = [] 
    for state in frontier:
        for perm in rubik.quarter_twists:
            s = rubik.perm_apply(perm, state)
            visited1[s[0]]=l
            parent[s[0]]=state
            new_frontier.append(s[0])
            if s[0] in visited2:
                flag = True#found in other frontier                
    frontier = new_frontier 
    return flag

def min_vertex(visited1, visited2):
    """finds the minimum vertices"""

    minv = None
    for key in visited1:
        if key in visited2:
            if minv is None:
                minv = key
            else:
                if((visited1[minv] + visited2[minv]) > \
                    (visited1[key] + visited2[key])):
                    minv = key
    return minv


def return_path(parent1, parent2, vertex):
    """for a given vertex construct an path"""
    path1 = []
    path2 = []
    v1 = parent1[vertex]
    while v1 is not None:
        path1.append(v1)
        v1 = parent1[v1]

    v2 = parent2[vertex]
    while v2 is not None:
        path2.append(v2)
        v2 = parent2[v2]
    
    path1.reverse()
    return path1 + [vertex] + path2



def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    visited1 = {start: 0} #frontier for first bfs along with level
    visited2 = {end: 0} #frontier for second bfs along with level

    parent1 = {start: None} #keeps the parent pointer of first bfs
    parent2 = {end: None} #keeps the parent pointer of second bfs

    frontier1 = [start] #frontier for first bfs
    frontier2 = [end] #frontier for second bfs
    
    l = 0 #keeps the left level
    r = 0 #keeps the right level
    while True:
        l +=1
        r +=1
        if(update_frontier(visited1, visited2, parent1, frontier1, l) or\
             update_frontier(visited2, visited1, parent2, frontier2, r)):
            break
    
    min = min_vertex(visited1, visited2) 
    return return_path(parent1, parent2, min)
    
