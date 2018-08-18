from fork import Fork
from deepSearch import DeepSearch
def main():
	fork = Fork() #objeto grafo instanciado
	#fork.degree_vertices()
	#fork.show_neighbors()
	deepSearch = DeepSearch(fork) #busca profunda deve receber um grafo para percorrer
	

if __name__ == "__main__":
    main()