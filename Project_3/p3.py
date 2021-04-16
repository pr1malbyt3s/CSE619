from collections import deque

# Reference: https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
# Breadth First Search function to perform BFS traversal on a set of provided vertices: 
def BFS(graph, source, destination):
    # Initiate an empty list which will capture explored vertices:
    explored = []
    # Create a queue object which will hold vertices to be explored: 
    queue = deque()
    # Add the source vertex to the queue:
    queue.append(source)
    # If the source and destination are the same, distance is zero:
    if source == destination:
        return 0
    # While the queue is not empty:
    while queue:
        # Create a path from the queue not including the parent vertex:
        path = queue.popleft()
        # Assess the vertex at the end of the path:
        vertex = path[-1]
        # If the vertex hasn't been explored:
        if vertex not in explored:
            # Get its neighbors from the graph:
            neighbors = graph[vertex]
            # Iterate through each neighbor:
            for neighbor in neighbors:
                # Form a new path from the current path:
                new_path = list(path)
                # Add the neighbor to the new path:
                new_path.append(neighbor)
                # Append the new path to the queue:
                queue.append(new_path)
                # Check if this neighbor is the destination:
                if neighbor == destination:
                    # If so, the number of nodes in the path minus 1 is the distance from source:
                    return len(new_path) - 1
            # Add the vertex to the explored list:
            explored.append(vertex)
    # If there is no path to destination, the distance is infinite:
    return 'Infinite'

# Breadth First Run function to facilitate conducting BFS for entire graph:
def BFS_Run(graph):
    # Dict to store the distances from source for each vertex:
    distance = {}
    # Iterate through the vertices:
    for vertex in graph:
        # Use BFS to get distance to each from source:
        distance[vertex] = BFS(graph, list(graph.keys())[0], vertex)
    # Print the BFS results using the vertex and its found distance:
    print("BFS Results")
    for key in distance:
        print("Vertex:", key, "\tDistance:", distance[key])
    print()

# Reference: https://www.techiedelight.com/arrival-departure-time-vertices-dfs/
# Depth First Search Function to perform DFS traversal on a provided graph vertex:
def DFS(graph, vertex, discovered, discover, finish, time):
    # Set time for capturing discover and finish times:
    time = time + 1
    # Set the discover/arrival time of vertex v:
    discover[vertex] = time
    # Mark currently assessed vertex as discovered:
    discovered[vertex] = True
    # Iterate through the graph edges for the vertex, repeating DFS is vertex not yet discovered:
    for letter in graph[vertex]:
        if not discovered.get(letter):
            time = DFS(graph, letter, discovered, discover, finish, time)
    # Increment the time to capture finishing for the vertex:
    time = time + 1
    # Set the finishing/departure time of vertex v:
    finish[vertex] = time
    # Return the time:
    return time

# Depth First Search Run function to facilitate conducting DFS for entire graph:
def DFS_Run(graph):
    # Dict to store the discover times of each vertex:
    discover = {}
    # Dict to store the finishing times of each vertex:
    finish = {}
    # Dict to store discovery of each vertex:
    discovered = {}
    # Set the start time to 0:
    time = 0
    # Perform DFS for all vertices and available edges in the graph:
    for vertex in graph:
        if not discovered.get(vertex):
            time = DFS(graph, vertex, discovered, discover, finish, time)
    # Print DFS results using D and F times of each vertex in DFS:
    print("DFS Results:")
    for key in graph:
        print("Vertex:", key, "\tDiscovery Time:", discover[key], "\tFinishing Time:", finish[key])
    # Print Topological Sorting using descending finishing times by vertex:
    print("\nTopological Sorting:")
    for k, v in sorted(finish.items(), key = lambda item: item[1], reverse=True):
        print("Vertex:", k, "\tFinishing Time:", v)
    print()
if __name__ == '__main__':
    # Graphs:
    graph1 = {'q':['s', 't', 'w'], 'r':['u', 'y'], 's':['v'], 't':['x', 'y'], 'u':['y'], 'v':['w'], 'w':['s'], 'x':['z'], 'y':['q'], 'z':['x']}
    graph2 = {'n':['o', 'q', 'u'], 'm':['q', 'r', 'x'], 'o':['r', 's', 'v'], 'p':['o', 's', 'z'], 'q':['t'], 'r':['u', 'y'], 's':['r'], 't':[], 'u':['t'], 'v':['w', 'x'], 'w':['z'], 'x':[], 'y':['v'], 'z':[]}
    # Run the BFS functions:
    BFS_Run(graph1)
    BFS_Run(graph2)
    # Run the DFS functions:
    DFS_Run(graph1)
    DFS_Run(graph2)
