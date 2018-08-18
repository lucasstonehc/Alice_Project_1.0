from fork import Fork
class DeepSearch(object):
	vertices = []
	def __init__(self, fork):
		self.vertices = fork.get_all_vertices()
		self.deep_search(self.vertices[0])

	def deep_search(self, vertice):
		vertice.setMarked(True)



	#def to_explore(self):

