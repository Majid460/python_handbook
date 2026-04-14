# Graphs are like the trees but they are less restricted and have cycles and multiple paths to reach a destination

# Graphs can be represented by adjacency metrix and list
"""
Visually:
0 ── 1 ── 3
│
2 ── 4

List: key value pair
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}
Matrix:
grid = [
    ["1","1","0","0"],
    ["1","1","0","1"],
    ["0","0","0","1"],
    ["0","0","0","0"]
]
"""
# I will create all types of graph creating methods
# 1. Adj Matrix - Un-directed and un-weighted
# 2. Adj Matrix - directed and un-weighted
# 3. Adj List - Un-directed and un-weighted
# 4. Adj List - directed and un-weighted


# 1.  Adj Matrix - Un-directed and un-weighted
from collections import deque
from typing import List, Any


class AdjMatrix:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.mat_undir = [
            [0 for _ in range(self.vertices)] for _ in range(self.vertices)
        ]
        self.mat_dir = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

    def create_undir(self, v_a, v_b):
        # As it is undirected so we need to add both ways
        self.mat_undir[v_a][v_b] = 1
        self.mat_undir[v_b][v_a] = 1

    def create_dir(self, v_a, v_b):
        # As it is undirected so we need to add both ways
        self.mat_dir[v_a][v_b] = 1

    def display(self, mat: List[List]):
        # [print(f"{item}", sep=" ", end=" ") for row in mat for item in row]
        for row in mat:
            for item in row:
                print(item, end=" ")
            print()


class AdjList:
    # key value pair
    def __init__(self, vertices: List[Any]) -> None:
        # if vertices are not numbers
        # vertices = ['a', 'b', 'c', 'd']
        self.vertices = vertices
        self.list_undir = {v: [] for v in self.vertices}
        self.list_dir = {v: [] for v in self.vertices}

    def create_undir(self, v_a, v_b):
        # from v_a -> v_b
        self.list_undir[v_a].append(v_b)

        # since the graph is undirected
        # from v_b -> v_a
        self.list_undir[v_b].append(v_a)

    def create_dir(self, v_a, v_b):
        # from v_a -> v_b
        self.list_dir[v_a].append(v_b)

    def display(self, adj_list: dict[Any, list]):
        for i in self.vertices:
            # Will give lists -> [....], [....]
            # Print the vertex
            print(f"{i}:", end=" ")
            # On that index in adj list get elements of array
            for j in adj_list[i]:
                # Print its adjacent
                print(j, end=" ")
            print()

    # BFS for traversal
    """
    a: b c 
    b: a c 
    c: a b 
    """

    def has_path(self, start, dest, graph):
        # Using bfs
        if start == dest:
            return True
        visited = {start}
        queue = deque([start])

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            if node == dest:
                return True  # If we reach to dest from start then path exists
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return False

    def dfs_has_path(self, graph, start, dest, visited):
        # Mark as visited immediately on entry
        if start == dest:
            return True
        visited.add(start)
        print(start)

        for neighbour in graph[start]:
            if neighbour not in visited and self.dfs_has_path(
                graph, neighbour, dest, visited
            ):  # ✅ use return value
                return True
        return False


# TimeO(V + E) — visit every vertex and edge once
# SpaceO(V) — visited set + queue at most hold all vertices


def connected_tree_bfs(start, graph):
    if not graph:
        return None
    # Init a queue
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        # Loop on neighbors
        for n in graph[node]:  # graph["a"] -> ["c","b"] this list is being iter
            if n not in visited:
                visited.add(n)
                queue.append(n)


def dis_connected_graph(graph, vertices):
    visited = set()
    components = []

    def bfs(start):
        queue = deque([start])
        visited.add(start)
        current_component = []

        while queue:
            node = queue.popleft()
            current_component.append(node)
            print(graph[node])
            for i, connected in enumerate(graph[node]):
                if connected == 1 and i not in visited:
                    visited.add(i)
                    queue.append(i)

        return current_component

    for n in vertices:
        if n not in visited:
            comp = bfs(n)
            components.append(comp)

    return components, len(components)


if __name__ == "__main__":
    adj_mat = AdjMatrix(6)
    edges = [[1, 0], [2, 0], [0, 3], [4, 5]]  # Edges between vertex a to b (a,b)
    # Un-directed Graph
    [
        adj_mat.create_undir(it[0], it[1]) for it in edges
    ]  # will create path between a-b and b-a
    print("Adj Matrix of Un-directed ::  ")
    adj_mat.display(adj_mat.mat_undir)

    # Directed Graph
    print("Adj Matrix of directed ::  ")
    [adj_mat.create_dir(it[0], it[1]) for it in edges]  # will create path between a-b
    adj_mat.display(adj_mat.mat_dir)

    # Adj List
    # Provide vertices and edges
    print("------ Adj List --------")
    vertices = ["a", "b", "c"]
    adj_list = AdjList(vertices)

    print("----- Adj List Un-dir ------")
    edges = [["a", "b"], ["a", "c"], ["b", "c"]]
    [
        adj_list.create_undir(it[0], it[1]) for it in edges
    ]  # will create path between a-b and b-a
    adj_list.display(adj_list.list_undir)

    print(" \n----- Has path BFS---- ")
    print(adj_list.has_path("a", "c", adj_list.list_undir))

    print(" \n----- Has path DFS---- ")
    print(adj_list.dfs_has_path(adj_list.list_undir, "a", "d", set()))

    print("----- Adj List dir ------")
    edges = [["a", "b"], ["a", "c"], ["b", "c"]]
    [adj_list.create_dir(it[0], it[1]) for it in edges]  # will create path between a-b
    adj_list.display(adj_list.list_dir)

    print("----- BFS Connected------")
    connected_tree_bfs(vertices[0], adj_list.list_dir)

    print("\n----- BFS dis - Connected graph------")
    res, com = dis_connected_graph(adj_mat.mat_undir, range(adj_mat.vertices))
    print()
    print(res, com)
