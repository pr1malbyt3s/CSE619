# Reference: https://www.techiedelight.com/arrival-departure-time-vertices-dfs/

# Function to perform DFS traversal on the graph on a graph.
def DFS(graph, v, discovered, discover, finish, time):
    # Set time for capturing discover and finish times
    time = time + 1
    # Set the discover/arrival time of vertex `v`
    discover[v] = time
    # Mark vertex as discovered
    discovered[v] = True
    # Iterate through the adjacency list for the vertex, repeating DFS if vertex not discovered
    for i in graph[v]:
        if not discovered[i]:
            print(i)
            time = DFS(graph, i, discovered, discover, finish, time)
    # Increment the time to capture finishing
    time = time + 1
    # Set the finishing/departure time of vertex `v`
    finish[v] = time
    # Return the time
    return time

def DFS_Run(graph):
    # Build a graph from the given edges
    #graph = Graph(edges, N)
    # List to store the discover times of each vertex
    discover = [None] * len(graph)
    # List to store the finishing times of each vertex
    finish = [None] * len(graph)
    # Mark all the vertices as not discovered initially
    discovered = [False] * len(graph)
    # Set the start time to 0
    time = 0
    # Perform DFS traversal from all undiscovered nodes to
    # cover all unconnected components of a graph
    for i in range(len(graph)):
        if not discovered[i]:
            time = DFS(graph, i, discovered, discover, finish, time)
    # Print D and F times of each vertex in DFS
    for i in range(len(graph)):
        print("Vertex", i, (discover[i], finish[i]))   
 
 
if __name__ == '__main__':
    # List of graph edges as per the reference diagram
    # q=0, r=1, s=2, t=3, u=4, v=5, w=6, x=7, y=8, z=9
    edges = [(0, 2), (0, 3), (0, 6), (1, 4), (1, 8), (2, 5), (3, 7), (3, 8), (4, 8), (5, 6), (6, 2), (7, 9), (8, 0), (9, 7)]
    # Total number of nodes in the graph
    graph = {0:[2, 3, 6], 1:[4, 8], 2:[5], 3:[7, 8], 4:[8], 5:[6], 6:[2], 7:[9], 8:[0], 9:[7]}
    DFS_Run(graph)
    
