from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                result.append(vertex)
                visited.add(vertex)
                queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)
        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS traversal starting from vertex 2:")
bfs_result = g.bfs(2)
print(bfs_result)

print("DFS traversal starting from vertex 2:")
dfs_result = g.dfs(2)
print(dfs_result)
