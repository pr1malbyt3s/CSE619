# Reference: https://www.techiedelight.com/arrival-departure-time-vertices-dfs/
# A class to represent a graph object
class Graph:
    def __init__(self, edges, N):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
# Function to perform DFS traversal on the graph on a graph
def DFS(graph, v, discovered, discover, finish, time):
 
    time = time + 1
 
    # set the arrival time of vertex `v`
    discover[v] = time
 
    # mark vertex as discovered
    discovered[v] = True
 
    for i in graph.adjList[v]:
        if not discovered[i]:
            time = DFS(graph, i, discovered, discover, finish, time)
 
    time = time + 1
 
    # set departure time of vertex `v`
    finish[v] = time
 
    return time
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    # q=0, r=1, s=2, t=3, u=4, v=5, w=6, x=7, y=8, z=9
    edges = [(0, 2), (0, 3), (0, 6), (1, 4), (1, 8), (2, 5), (3, 7), (3, 8), (4, 8), (5, 6), (6, 2), (7, 9), (8, 0), (9, 7)]
 
    # total number of nodes in the graph
    N = 10
 
    # build a graph from the given edges
    graph = Graph(edges, N)
 
    # list to store the arrival time of vertex
    discover = [None] * N
 
    # list to store the departure time of vertex
    finish = [None] * N
 
    # Mark all the vertices as not discovered
    discovered = [False] * N
    time = 0
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all unconnected components of a graph
    for i in range(N):
        if not discovered[i]:
            time = DFS(graph, i, discovered, discover, finish, time)
 
    # print arrival and departure time of each vertex in DFS
    for i in range(N):
        print("Vertex", i, (discover[i], finish[i]))
