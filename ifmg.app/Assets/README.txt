Autor: Lucas Santos Pimenta Junior
IFMG-Sabará
Algorítmo implementado:
    Arvores Geradoras: PRIM

Pseudocódigo do algorítmo:
    Ler G= (N,M)e D = [dij] a matriz de pesos deG
    Escolha qualquer vertice i ∈ N
    T←{i}
    V←N\{i}
    Tmin←∅
    Enquanto T != N Faca
        Encontrar a aresta (j,k)∈ M tal que j∈T, k∈V e Djk ́e mínimo
        T←T∪{k}
        V←V\{k}
        Tmin←Tmin∪(j,k)
    Fim Enquanto
    Escrever Tmin {o conjunto das arestas da  ́arvore geradora mínima}
    Professor:  Carlos Alexandre   (IFMG)Teoria dos Grafos4 / 39


Objetivo:
    Apresentar de forma mais tangível, o que foi estudado em sala de aula!

Desafios encontrados durante a implementação:
    *Entender o domínio do algorítmo
    *Modelar o problema
    *Transformar o pseudocódigo para código de máquina