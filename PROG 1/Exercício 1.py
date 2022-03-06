# (a) Leia n, m inteiros n>0, m>=0 e as arestas ij, i>j em {0,1,2,...,n-1}=V
#      Peça o nome do grafo G. (dado pelo usuário)
#     Armazene G=(V,E) na memória.
#    Imprima a matriz de adjacências M{nxn}.


def variaveis():
    n = le_n()
    m = le_m()
    g_name = le_nome_grafo()
    v = []
    v_aux = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for i in range(n):
        v.append(v_aux[i])
    e = le_e()
    g = (v, e)
    return n, m, g_name, g, v, e


def printar_matriz(M, n, m, v):
    print("     ", end="")
    for j in range(n):
        print("", end="")
        print(v[j], " ", end="")
    print()
    for i in range(n):
        print(v[i]," | ", end="")
        for j in range(m):
            print(M[i][j], " ", end="")
        print(" |", end="")
        print()


def salvar_grafo(g,g_name):
    name = g_name + ".txt"
    arq = open(name, 'w')
    for i in g[0]:
        arq.write(i)
        arq.write(" ")
    arq.write('\n')
    for j in g[1]:
        arq.write(j[0])
        arq.write(j[1])
        arq.write('\n')
    arq.close()


def main():
    n, m, g_name, g, v, e = variaveis()
    M = [None] * n

    for x in range(n):
        M[x] = [None] * m
        for y in range(m):
            M[x][y] = 0
            for z in e:
                if (z[0] == v[x] and z[1] == v[y]) or (z[0] == v[y] and z[1] == v[x]):
                    M[x][y] = 1
    printar_matriz(M, n, m, v)
    salvar_grafo(g,g_name)


def le_n():
    n = int(input("Digite N: "))
    if n <= 0:
        print("Erro, N precisa ser maior que 0")
        return le_n()
    return n


def le_m():
    m = int(input("Digite M: "))
    if m < 0:
        print("Erro, M precisa ser maior ou igual a 0")
        return le_m()
    return m


def le_nome_grafo():
    g = input("Digite o nome do Grafo: ")
    return g


def le_e():
    e = []
    print("Flag = espaço em branco")
    while True:
        edge = input("Digite o vertice de partida e o vertice de chegada da aresta (ex: ab): ")
        if edge == "":
            break
        elif len(edge) != 2:
            print("Erro, tente de novo")
            return le_e()
        e.append([edge[0],edge[1]])
    return e


main()
