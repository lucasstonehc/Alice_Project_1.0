from vertice import Vertice

class Fork(object):
	#grafo apresenta um numero de vertices e arestas
	vertices = []
	edges = []

	def __init__(self):
		self.create_fork()

	def create_fork(self): #criando o grafo
		file  = open("contents.txt",'r') #abrir o arquivo para leitura
		size = int(file.readline()) #size armazena o valor de quantos vertices sera criado
		self.create_vertices(size) #criando n vertices
		index = 0
		for line in file:
			informations = line.split(";")
			self.create_neighbors(informations, size, index)
			index+=1

		file.close()
		self.fill_degree()

	#preenchendo os vizinhos
	def create_neighbors(self, informations, size, index): #informations carrega as relações se há vizinho ou nao
		for i in range(size):
			if informations[i] == '1' or informations[i] == '1\n' :
				self.vertices[index].setNeighbors(self.vertices[i])
				

	def create_vertices(self, size):#criando os vertices
		i = 0
		while i < size:
			vertice = Vertice(i)
			self.vertices.append(vertice) #preenchendo minha lista com os vertices criados
			i+=1

	def fill_degree(self):
		for i in range(len(self.vertices)):
			degree = len(self.vertices[i].getNeighbors()) #quantos vizinhos -> grau
			self.vertices[i].setDegree(degree)
	
	def degree_vertices(self):
		for i in range(len(self.vertices)):
			print("vertice ",self.vertices[i].getId(),"possui grau ",self.vertices[i].getDegree())

	def show_neighbors(self):
		for i in range(len(self.vertices)):
			neighbors = self.vertices[i].getNeighbors()
			print("\nvizinhos do vertice ",self.vertices[i].getId())
			j = 0
			while j < len(neighbors):
				print(neighbors[j].getId())
				j+=1

	def get_all_vertices(self):
		return self.vertices