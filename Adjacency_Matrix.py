class AdjacencyMatrixGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start, end):
        # Assuming a simple, undirected graph
        self.graph[start][end] = 1
        self.graph[end][start] = 1

    def print_graph(self):
        for row in self.graph:
            print(row)



num_vertices = 5
matrix_graph = AdjacencyMatrixGraph(num_vertices)
matrix_graph.add_edge(0, 1)
matrix_graph.add_edge(0, 4)
matrix_graph.add_edge(1, 3)
matrix_graph.add_edge(3, 4)

print("Adjacency Matrix:")
matrix_graph.print_graph()
