import random

# entradas
qtd_vertices = int(input("Quantidade de vertices: "))
qtd_arcos = int(input("Quantidade de arcos: "))
peso_max = int(input("Peso máximo dos arcos: "))

if(qtd_arcos < qtd_vertices * (qtd_vertices-1)):
    #criação da matriz
    matriz_adj = []
    for i in range(qtd_vertices):
        matriz_adj.append(['inf'] * qtd_vertices)
        matriz_adj[i][i] = 0

    #criação dos arcos
    arcos_criados = 0
    while (arcos_criados < qtd_arcos):
        for i in range(qtd_vertices):
            vertice1 = i
            vertice2 = round(random.random()*qtd_vertices)-1
            if(matriz_adj[vertice1][vertice2] == 'inf'):
                peso = round(random.random() * peso_max)
                matriz_adj[vertice1][vertice2] = peso
                arcos_criados += 1

    # mostrar a matriz
    print("Quantidade de vertices:      " + str(qtd_vertices))
    print("Quantidade de arcos:         " + str(qtd_arcos))
    print("Quantidade de arcos criados: " + str(arcos_criados))
    for i in matriz_adj:
        print(i)
else:
    print("Quantidade de arcos inválida")