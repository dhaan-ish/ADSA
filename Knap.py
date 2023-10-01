class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    finalvalue = 0.0
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * W / item.weight
            break
    return finalvalue

def printJobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = [False] * t
    job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    print(job)

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = list(range(self.V))
        rank = [0] * self.V
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        print("Kruskal Algorithm Output :")
        for u, v, weight in result:
            print("Edge:", u, v, end=" ")
            print("-", weight)

def mst_find(G, s):
    distance = [float("inf")] * len(G)
    distance[s] = 0
    itr = [False] * len(G)
    c = 0
    while True:
        min_weight = float("inf")
        m_idx = -1
        for i in range(len(G)):
            if itr[i] == False:
                if distance[i] < min_weight:
                    min_weight = distance[i]
                    m_idx = i
        if m_idx == -1:
            break
        c += min_weight
        itr[m_idx] = True
        for i, j in G[m_idx].items():
            distance[i] = min(distance[i], j)
    return c

def primsAlgorithm(n, edges, s):
    G = {i: {} for i in range(n)}
    for item in edges:
        u = item[0]
        v = item[1]
        w = item[2]
        u -= 1
        v -= 1
        try:
            min_weight = min(G[u][v], w)
            G[u][v] = min_weight
            G[v][u] = min_weight
        except KeyError:
            G[u][v] = w
            G[v][u] = w
    return mst_find(G, s)

arr = [Item(90, 15), Item(150, 20), Item(180, 45)]
max_val = fractionalKnapsack(50, arr)
print("Fractional Knapsack Solution :", max_val)

arrTask = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27], ['d', 1, 25], ['e', 3, 15]]
print("Job Sequence Result :", end=' ')
printJobScheduling(arrTask, 3)

g = Graph(5)
g.add_edge(0, 1, 13)
g.add_edge(0, 2, 14)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 16)
g.add_edge(2, 4, 12)
g.add_edge(3, 4, 17)
g.kruskal()

print("Prim's Algorithm Result:", primsAlgorithm(4, [(1, 2, 5), (1, 3, 5), (2, 3, 7), (1, 4, 4)], 3))

class Dijkstra:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Dijkstra's Algorithm Solution:\nVertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = float("inf")
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

d = Dijkstra(9)
d.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
d.dijkstra(0)
