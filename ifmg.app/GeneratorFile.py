
class GeneratorFile(object): #classe irá preencher a classe grafo

    def __init__(self):
        self.path = ""
        self.matrix = []
        self.fill_matrix()
        #self.show_matrix()

    def getMatrix(self):
        return self.matrix

    def open_file(self):
        file = open("graph.txt", "r")
        if file.mode == 'r':
            return file

    def close_file(self, file):
        file.close()

    def size_of_matrix(self): #função retorna o tamanho que minha matriaz vai possuir
        file = self.open_file()
        line = file.readline()
        size = len(line.replace(' ', '').strip('\n'))
        self.close_file(file)
        return size


    def fill_matrix(self):
        size = self.size_of_matrix() #recebendo o tamanho da minha matriz
        file = self.open_file() #abre o arquivo
        for file_line in file.readlines():
            row = []
            line = self.line_split(file_line)
            for j in range(size):
                row.append(line[j])
            self.matrix.append(row)
        self.close_file(file) #fecha o arquivo


    def line_split(self, line):
        my_array = line.strip("\n").split(" ")
        row = []
        for item in my_array:
            row.append(item)
        return row

    def show_matrix(self):
        for i in range(self.size_of_matrix()):
                print(self.matrix[i], " ")
