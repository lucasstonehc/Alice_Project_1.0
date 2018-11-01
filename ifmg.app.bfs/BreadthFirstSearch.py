
from Graph import Graph
class BreadthFirstSearch(object):

    def __init__(self, graph, vertex):
        self.graph = graph
        self.vertices = self.graph.getVertices()
        self.Q = [] #lista para preencher de vertices
        self.vertex = vertex #este é o vertice inicial
        self.vertex.setMarked() #marcando o vertice
        #preencher a lista com o vertice inicial
        self.add_vertex_in_Q(self.vertex)

        while len(self.Q) != 0:
            self.vertex_u = self.pop_vertex_in_Q() #pegando o primeiro vertice na lista Q
            self.not_marked()

    def add_vertex_in_Q(self, vertex): #enfileira
        self.Q.append(vertex)

    def pop_vertex_in_Q(self): #desenfileira
        return self.Q.pop(0)

    def not_marked(self): #pega os vizinhos de vertice U
        neighbors = []
        neighbors_ids = self.vertex_u.getNeighbors() #retornando os IDs
        for id in neighbors_ids:
            neighbors.append(self.graph.getVertex(id)) #aqui estou pegando a instacia de vertex
            #adicionado na lista as instancia ...

        for neighbor_vertex in neighbors:
            if neighbor_vertex.getMarked() == False: #se o vertice vizinho nao for marcado entao devo marca-lo
                neighbor_vertex.setMarked()
                self.add_vertex_in_Q(neighbor_vertex) # e adiciona o vertice na lista

    def get_all_vertices(self):
        return self.vertices



graph = Graph()
bfs = BreadthFirstSearch(graph,graph.getVertex(0)) #instanciando o objeto bfs

for vertex in bfs.get_all_vertices():
    print("Vertice ",vertex.getId()," Marcado ", vertex.getMarked())

