Autor: Lucas Santos Pimenta Junior
IFMG-Sabará
Algorítmo implementado:
    Busca em largura, conhecido em Inglês como "Breadth First Search"
    Sigla: BFS

Pseudocódigo do algorítmo:
    BFS(grafo, verticeInicial)

        marque(verticeInicial)
        enfileira(Q, verticeInicial)
        enquanto Q for não nulo faça
            vertice_atual <- desenfileira(Q)
            enquanto houver vertice não marcado adjacente a vertice vertice_atual faça
                marque(vertice)
                 enfileira(Q, vertice)


Objetivo:
    Apresentar de forma mais tangível, o que foi estudado em sala de aula!


Desafios encontrados durante a implementação:
    *Entender o domínio do algorítmo
    *Modelar o problema
    *Transformar o pseudocódigo para código de máquina




