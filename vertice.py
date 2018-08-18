class Vertice(object):
	
	#construct
	def __init__(self, _id):
		self._id = _id
		self.degree = None # grau do vertice
		self.marked = False # vertice marcado
		self.neighbors = [] #lista de vizinhos

	#setter and getter id
	def getId(self):
		return self._id
	
	def setId(self, _id):
		self._id = _id

	#setter and getter neighbors
	def getNeighbors(self):
		return self.neighbors
	
	def getNeighbor(self, index):
		return self.neighbors[index]

	def setNeighbors(self, neighbor):
		self.neighbors.append(neighbor)

	#setter and getter degree
	def getDegree(self):
		return self.degree
	
	def setDegree(self, degree):
		self.degree = degree

	#setter and getter marked
	def getMarked(self):
		return self.marked

	def setMarked(self, marked):
		self.marked = marked