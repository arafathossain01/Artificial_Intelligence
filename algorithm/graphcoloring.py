class GraphColoring:

    def __init__(self):
        self.V = 0
        self.numOfColors = 0
        self.color = []
        self.graph = []

    def graphColor(self, g, k):

        self.V = len(g)
        self.numOfColors = k
        self.graph = g
        self.color = [0] * self.V

        if self.solve(0):
            print("\nSolution exists")
            self.display()
        else:
            print("\nNo solution")

    def solve(self, v):

        if v == self.V:
            return True

        for c in range(1, self.numOfColors + 1):

            if self.isPossible(v, c):

                self.color[v] = c

                if self.solve(v + 1):
                    return True

               
                self.color[v] = 0

        return False

    def isPossible(self, v, c):

        for i in range(self.V):

            if self.graph[v][i] == 1 and self.color[i] == c:
                return False

        return True

    def display(self):

        print("\nColors:", end=" ")

        for i in range(self.V):
            print("Color", self.color[i], end=" ")

        print()


N = int(input("Enter number of vertices: "))
M = int(input("Enter number of edges: "))
K = int(input("Enter number of colors: "))


graph = []

for i in range(N):
    graph.append([0] * N)


print("\nEnter the edges:")

for i in range(M):

    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1

gc = GraphColoring()


gc.graphColor(graph, K)