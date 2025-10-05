# Shortest-Path-find-using-dijkstra-algorithm
using dijkstra algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w  # For undirected graph

    def min_distance(self, dist, visited):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_val and not visited[v]:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V
        parent = [-1] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and not visited[v] and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u

        return dist, parent

    def print_path(self, parent, j):
        if parent[j] == -1:
            print(j, end="")
            return
        self.print_path(parent, parent[j])
        print(" ->", j, end="")

    def display_result(self, src, dist, parent):
        print("\nVertex\tDistance\tPath")
        for i in range(self.V):
            print(f"{src} -> {i}\t {dist[i]}\t\t", end="")
            self.print_path(parent, i)
            print()

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    g = Graph(n)

    e = int(input("Enter number of edges: "))
    print("Enter each edge as: u v weight")
    for _ in range(e):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    src = int(input("Enter source vertex: "))
    dist, parent = g.dijkstra(src)
    g.display_result(src, dist, parent)
