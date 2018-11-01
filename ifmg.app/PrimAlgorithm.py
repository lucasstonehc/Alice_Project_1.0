from Graph import Graph
from Vertex import Vertex



class PrimAlgorithm(object):

    def __init__(self):
        self.graph = Graph()  # instancia do grafo
        self.vertices = self.graph.getVertices()  # recebendo todos os vertices do grafo
        self.edges = self.graph.getEdges()  # todas as arestas do grafo
        self.T = []  # lista de T
        # init T
        self.T.append(self.vertices[0].getId())  # init com ID do primeiro vertice
        self.V = []  # todos os vertices menos o primeiro
        for vertex in self.vertices:
            self.V.append(vertex.getId())

        self.V.remove(self.T[0])

        self.T_min = []  # init T_min
        self.index = 0

        edge = self.edge_minimum_weight(self.T, self.V)
        #print(edge)
        while len(self.T) != len(self.vertices):
            edge = self.edge_minimum_weight(self.T, self.V)
            k = edge.getVerticeY()
            self.add_next_vertex_in_T(k) #adicionando vertice k
            self.remove_vertex_in_V(k)
            self.add_edge_in_Tmin(edge)
            #self.index = self.index + 1

        self.prim_path_show()


    def edge_minimum_weight(self, T, V): #index e para percorrer T recebe os vetores, V que é um vetor de vertices
        list_of_edges = []
        for j in T:
            for k in V:
                answer = self.edge_find(j,k)
                if answer != None:
                    list_of_edges.append(answer)


        weight = list_of_edges[0].getWeight()
        edge_final = list_of_edges[0]

        for edge in range(len(list_of_edges)):
            if list_of_edges[edge].getWeight() < weight:
                weight = list_of_edges[edge].getWeight()
                edge_final = list_of_edges[edge]

        return  edge_final

    def edge_find(self, j, k): #recebe os vertices
        edge = self.graph.getEdge(j,k)
        if edge != None:
            return edge #retorna a aresta

    def add_next_vertex_in_T(self, k):
        self.T.append(k)


    def remove_vertex_in_V(self, k):
        self.V.remove(k)

    def add_edge_in_Tmin(self, edge):
        self.T_min.append(edge)

    def prim_path_show(self):
        print("Arvore geradora minima e \n")
        edges = self.T_min
        for edge in edges:
            print("(",edge.getVerticeX(),",",edge.getVerticeY(),")\n")


primAlgorithm = PrimAlgorithm()

