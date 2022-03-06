def Busca(elemento_procurado,fonte):
    #print(f"vou buscar {elemento_procurado}\nem\n{fonte}")
    try:
        val = fonte.index(elemento_procurado)
        #print(f"achei {val}\n")
    except:
        val = -1
        #print("não achei\n")
    return val

def cria_grafo(nome_grafo):
    vertices=[]
    arestas=[]
    #Pega os vertices
    print("Digite a quantidade de vertices do grafo (Se não houver digite ENTER):")
    n = int(input())
    print("Digite a quantidade de arestas do grafo (Se não houver digite ENTER):")
    m = int(input())


    for i in range(0,n):
        #print(f"Digite o vertice {i} do grafo:")
        #temp = input()
        vertices.append(i)
        if(temp == ""):
            vertices.pop(-1)
            break
            #Pega as arestas
    for j in range(0,m):
        print(f"Digite os dois vertices que compoem a aresta {j} do grafo no seguinte formato:\nv1 v2")
        temp = input()
        arestas.append(temp)
        if(temp == ""):
            arestas.pop(-1)
            break
    return vertices, arestas


def completo(n):
    m = (n*n)-n
    vertices=[]
    arestas=[]
    for i in range(0,n):
        vertices.append(str(i))
    for i in range(0,n):
        for j in range(0,n):
            if(int(i) != int(j)):
                aux = f"{i} {j}"
                arestas.append(str(aux))
    return vertices, arestas

def star(m):
        n = m+1
        vertices=[]
        arestas=[]
        for i in range(0,n):
            vertices.append(str(i))
        for i in range(0,n):
            if(int(i) != 0):
                aux = f"0 {i}"
                arestas.append(str(aux))
        return vertices, arestas

def caminho(n):
        m = n-1
        vertices=[]
        arestas=[]
        for i in range(0,n):
            vertices.append(str(i))

        for i in range(1,n):
            if(int(i) != 0):
                aux = f"{i-1} {i}"
                arestas.append(str(aux))
        return vertices, arestas


def ciclo(n):
        m = n
        vertices=[]
        arestas=[]
        for i in range(0,n):
            vertices.append(str(i))

        for i in range(1,n):
            if(int(i) != 0):
                aux = f"{i-1} {i}"
                arestas.append(str(aux))
        aux = f"{n} {0}"
        arestas.append(str(aux))
        return vertices, arestas

def whel(n):
        m = 2*n
        vertices=[]
        arestas=[]
        for i in range(0,n):
            vertices.append(str(i))

        #ciclo
        for i in range(0,n):
            if(int(i) != 0):
                aux = f"0 {i}"
                arestas.append(str(aux))

        for i in range(1,n-1):
            if(int(i) != 0):
                aux = f"{i} {i+1}"
                arestas.append(str(aux))
        aux = f"{n-1} {1}"
        arestas.append(str(aux))
        return vertices, arestas

def bipartido(s1,s2):
    vertices = []
    arestas = []
    k = [] #s1
    l = [] #s2
    for i in range(0,s1):
        aux = f"a{i}"
        k.append(aux)

    for i in range(0,s2):
        aux = f"b{i}"
        l.append(aux)

    vertices = k + l

    for i in k:
        for j in l:
            aux = f"{i} {j}"
            arestas.append(aux)

    return vertices,arestas

def cubo(d):
    vertices = []
    arestas = []
    aux = 2**d

    for i in range(0,aux):
        vertices.append(str("{0:b}".format(i)).zfill(d))
    for i in range(0,len(vertices)):
        diferente = 0
        for j in range(0,len(vertices)):
            if(vertices[i] != vertices[j]):
                #print(f"{vertices[i]} != {vertices[j]}\n")
                v1 = vertices[i]
                v2 = vertices[j]
                for k in range(0,d):
                    #print(f"{v1[k]} {v2[k]}\n")
                    if(v1[k] != v2[k]):
                        diferente +=1
                #print(f"diferente = {diferente}\n")
                if(diferente == 1):
                    aux = f"{v1} {v2}"
                    aux2 = f"{v2} {v1}"
                    if(Busca(aux2,arestas) == -1):
                        arestas.append(aux)
            diferente = 0
    return vertices, arestas

v, a= cubo(3)
print(v)
print(a)
