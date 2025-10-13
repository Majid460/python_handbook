"""
A UndiAndUnWGraph is a non-linear data structure that consists of vertices (nodes) and edges.

A vertex, also called a node, is a point or an object in the UndiAndUnWGraph, and an edge is used to connect two vertices with each other.
Graphs are non-linear because the data structure allows us to have different paths to get from one vertex to another, unlike with linear data structures like Arrays or Linked Lists.
Graphs are used to represent and solve problems where the data consists of objects and relationships between them, such as:

Social Networks: Each person is a vertex, and relationships (like friendships) are the edges. Algorithms can suggest potential friends.
Maps and Navigation: Locations, like a town or bus stops, are stored as vertices, and roads are stored as edges. Algorithms can find the shortest route between two locations when stored as a UndiAndUnWGraph.
Internet: Can be represented as a UndiAndUnWGraph, with web pages as vertices and hyperlinks as edges.
Biology: Graphs can model systems like neural networks or the spread of diseases.

A weighted UndiAndUnWGraph is a UndiAndUnWGraph where the edges have values. The weight value of an edge can represent things like distance, capacity, time, or probability.
A connected UndiAndUnWGraph is when all the vertices are connected through edges somehow. A UndiAndUnWGraph that is not connected, is a UndiAndUnWGraph with isolated (disjoint) subgraphs, or single isolated vertices.
A directed UndiAndUnWGraph, also known as a digraph, is when the edges between the vertex pairs have a direction. The direction of an edge can represent things like hierarchy or flow.

A cyclic UndiAndUnWGraph is defined differently depending on whether it is directed or not:

A directed cyclic UndiAndUnWGraph is when you can follow a path along the directed edges that goes in circles. Removing the directed edge from F to G in the animation above makes the directed UndiAndUnWGraph not cyclic anymore.
An undirected cyclic UndiAndUnWGraph is when you can come back to the same vertex you started at without using the same edge more than once. The undirected UndiAndUnWGraph above is cyclic because we can start and end up in vertes C without using the same edge twice.
A loop, also called a self-loop, is an edge that begins and ends on the same vertex. A loop is a cycle that only consists of one edge. By adding the loop on vertex A in the animation above, the UndiAndUnWGraph becomes cyclic.
"""
"""
UndiAndUnWGraph Representation

1. Adjacency Matrix UndiAndUnWGraph Representation:
   Adjacency Matrix is the UndiAndUnWGraph representation (structure) we will use for this tutorial.
   How to implement an Adjacency Matrix is shown on the next page.
   The Adjacency Matrix is a 2D array (matrix) where each cell on index (i,j) stores information about the edge from vertex i to vertex j.
   Below is a UndiAndUnWGraph with the Adjacency Matrix representation next to it.
2. Adjacency List UndiAndUnWGraph Representation
   In case we have a 'sparse' UndiAndUnWGraph with many vertices, we can save space by using an Adjacency List compared to using an Adjacency Matrix, because an Adjacency Matrix would reserve a lot of memory on empty Array elements for edges that don't exist.
   A 'sparse' UndiAndUnWGraph is a UndiAndUnWGraph where each vertex only has edges to a small portion of the other vertices in the UndiAndUnWGraph.
   An Adjacency List has an array that contains all the vertices in the UndiAndUnWGraph, and each vertex has a Linked List (or Array) with the vertex's edges.
"""
# To implement the graph i am going to use class, it will add an extra abstraction layer
"""
UndiAndUnWGraph important params:
1. Vertices data
2. Adjacency matrix or list
3. Size of vertices list
"""
"""
Graphs Traversal
To traverse a Graph means to start in one vertex, and go along the edges to visit other vertices until all vertices, or as many as possible, have been visited.

Understanding how a Graph can be traversed is important for understanding how algorithms that run on Graphs work.

The two most common ways a Graph can be traversed are:

Depth First Search (DFS)
Breadth First Search (BFS)
DFS is usually implemented using a Stack or by the use of recursion (which utilizes the call stack), while BFS is usually implemented using a Queue.
"""


# 1. Implementation for undirected and unweighted graph
def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ", sep=",")
        print()  # new line


class UndiAndUnWGraph:
    def __init__(self, size):
        self.adjacency_matrix = [[0] * size for _ in
                                 range(size)]  # 2D array with initial values is 0 for adjacency matrix
        self.vertices_data = [''] * size
        self.size = size

    # To add vertex in the list of vertices
    def add_vertex_data(self, vertex, data) -> bool:
        if 0 <= vertex < self.size:  # if the vertex is greater or equal to 0 and less then the size of the vertex array
            self.vertices_data[vertex] = data
            return True
        else:
            return False

    # To add edges between vertices
    def add_edge(self, v_i: int, v_j: int) -> bool:  # Pass the vertex i index and vertex j index to add edge
        if 0 <= v_i < self.size and 0 <= v_j < self.size:
            # I am considering a undirected graph at this stage so thats why i assigned the 1 for A - B and B - A
            self.adjacency_matrix[v_i][v_j] = 1  # e.g. Edge from A to B
            self.adjacency_matrix[v_j][v_i] = 1  # e.g. Edge from B to A
            return True
        else:
            return False

    # Display the graph
    def display(self):
        print("\n ---------- Adjacency Matrix-------------")
        [print(' '.join(map(str, row))) for row in self.adjacency_matrix]
        print("---------- Vertex Data-------------")
        for vertex, data in enumerate(self.vertices_data):
            print(f" Vertex {vertex} -> {data if data is not None else 0}")

    # DFS - Graph traversal using stack
    def dfs_traversal(self, start_index):
        visited = [False] * self.size  # Track for the visited vertices
        stack = [start_index]
        while stack:
            node = stack.pop()
            if not visited[node]:
                print(self.vertices_data[node], end=" ")
                visited[node] = True

                # Add neighbors in reverse to maintain order
                for neighbor_index in reversed(self.size):
                    if self.adjacency_matrix[node][neighbor_index] != 0 and not visited[neighbor_index]:
                        stack.append(neighbor_index)

    # Cycle detection using DFS
    def has_cycle(self):
        """
        Keeps track of which vertices have been visited.
        self.size = number of vertices in your graph.
        Initially, all set to False.
        """
        visited = [False] * self.size

        # DFS Helper function
        def dfs(v, parent):
            # Mark current node v as visited.
            """
            :param v: Vertex index
            :param parent: keeps track of the node we came from (so we don’t count the same edge twice)
            :return: True if already visited so has a cycle
            """
            visited[v] = True
            """
            Check adjacency matrix row for v
            If self.adjacency_matrix[v][u] != 0, then there’s an edge v — u (could be weighted, not just 1).
            """
            # Explore the neighbors
            for u in range(self.size):
                if self.adjacency_matrix[v][u] != 0:  # edge exists between v and u
                    # Check for cycle
                    """
                    If neighbor u has not been visited → DFS deeper.
                    If neighbor u is visited already and u != parent → cycle detected.
                    Why? Because if u isn’t the parent, it means there’s another way back to u, forming a loop.
                    """
                    if not visited[u]:
                        if dfs(u, v):
                            return True
                    elif u != parent:
                        return True

        """
        Graph might be disconnected (multiple components).
        Run DFS from every unvisited node.
        parent = -1 means root (no parent at start).
        """
        for v in range(self.size):
            if not visited[v]:
                if dfs(v, -1):
                    return True

        return False


# 1. Implementation for directed and weighted graph
class DirAndWeGraph:
    def __init__(self, size):
        self.adjacency_matrix = [[None] * size for _ in
                                 range(size)]  # 2D array with initial values is None for adjacency matrix
        self.vertices_data = [''] * size
        self.size = size

    # To add vertex in the list of vertices
    def add_vertex_data(self, vertex, data) -> bool:
        if 0 <= vertex < self.size:  # if the vertex is greater or equal to 0 and less then the size of the vertex array
            self.vertices_data[vertex] = data
            return True
        else:
            return False

    # To add edges between vertices
    def add_edge(self, v_i: int, v_j: int,
                 weight: int) -> bool:  # Pass the vertex i index and vertex j index to add edge
        if 0 <= v_i < self.size and 0 <= v_j < self.size:
            # I am considering a directed graph at this stage so that's why i assigned the weight for A - B
            self.adjacency_matrix[v_i][v_j] = weight  # e.g. Edge from A to B with the weight
            return True
        else:
            return False

    # Display the graph
    def display(self):
        print("\n ---------- Adjacency Matrix-------------")
        [print(' '.join(map(lambda x: str(x) if x is not None else '0', row))) for row in self.adjacency_matrix]
        print("---------- Vertex Data-------------")
        for vertex, data in enumerate(self.vertices_data):
            print(f" Vertex {vertex} -> {data}")

    # BFS -> Queue based traversal
    def bfs_traversal(self, start_vertex_data):
        queue = [self.vertices_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
        order = []

        while queue:
            current_vertex = queue.pop(0)
            order.append(self.vertices_data[current_vertex])
            for i in range(self.size):
                if self.adjacency_matrix[current_vertex][i] != 0 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print(" -> ".join(order))

        # Cycle detection using DFS

    # Cycle detection in the directed graph

    def has_cycle(self):
        """
        Keeps track of which vertices have been visited.
        self.size = number of vertices in your graph.
        Initially, all set to False.
        visited[v] → True if vertex v has been fully explored.
        rec_stack = True if vertex v is in the current DFS recursion path (call stack).
        """
        visited = [False] * self.size
        rec_stack = [False] * self.size

        # For directed graphs, a cycle means we find a back edge to a vertex that’s still in the recursion stack.
        # DFS Helper function
        def dfs(v):
            # Mark current node v as visited.
            """
            :param v: Vertex index
            :return: True if already visited so has a cycle
            """
            # When we enter a vertex v, we mark it as visited and put it in the recursion stack.
            visited[v] = True
            rec_stack[v] = True
            """
            Check adjacency matrix row for v
            If self.adjacency_matrix[v][u] != 0, then there’s an edge v — u (could be weighted, not just 1).
            """
            # Explore the neighbors
            for u in range(self.size):
                """
                Look at row v in the adjacency matrix.
                If there’s a nonzero entry → directed edge from v → u.
                """
                if self.adjacency_matrix[v][u] != 0:  # edge exists between v and u
                    # Check for cycle
                    """
                    If neighbor u is not visited → recurse DFS on it.
                    If neighbor u is already in recursion stack (rec_stack[u] == True) → we found a back edge, meaning there’s a cycle.
                    """
                    if not visited[u]:
                        if dfs(u):
                            return True
                    elif rec_stack[u]:  # back edge → cycle
                        return True
            rec_stack[v] = False
            return False
        for v in range(self.size):
            if not visited[v]:
                if dfs(v):
                    return True

        return False


if __name__ == '__main__':
    print("---------- Undirected and Unweighted Graph--------------")
    g = UndiAndUnWGraph(4)
    g.add_vertex_data(0, 'A')
    g.add_vertex_data(1, 'B')
    g.add_vertex_data(2, 'C')
    g.add_vertex_data(3, 'D')
    g.add_edge(0, 1)  # A - B
    g.add_edge(0, 2)  # A - C
    g.add_edge(0, 3)  # A - D
    g.add_edge(1, 2)  # B - C

    g.display()
    print_connections(g.adjacency_matrix, g.vertices_data)
    print("---------- Cycle In Undirected--------------")
    print(f"Has cycle => {g.has_cycle()}")

    print("---------- Directed and weighted Graph--------------")
    dir = DirAndWeGraph(4)
    dir.add_vertex_data(0, 'A')
    dir.add_vertex_data(1, 'B')
    dir.add_vertex_data(2, 'C')
    dir.add_vertex_data(3, 'D')
    dir.add_edge(0, 1, 3)  # A -> B with weight 3
    dir.add_edge(0, 2, 2)  # A -> C with weight 2
    dir.add_edge(3, 0, 4)  # D -> A with weight 4
    dir.add_edge(2, 1, 1)  # C -> B with weight 1

    dir.display()
    print_connections(dir.adjacency_matrix, dir.vertices_data)
    print("\n ---------- BFS Traversal-------------")
    dir.bfs_traversal('D')
    print("\n ---------- Cycle-------------")
    print(f"Has cycle => {g.has_cycle()}")