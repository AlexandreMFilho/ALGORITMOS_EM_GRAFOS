
vertices=[]
arestas=[]
matriz_ad=[]


def imprime_matriz(lista_de_1,n):
    lim=len(n)
    sinal =0
    for i in range(0,lim):
        print("[",end=" ")
        for j in range(0,lim):
            for k in range(0,len(lista_de_1)):
                #Vê na lista se o indice [i][j] atual existe nela se sim print 1 se não print 0
                v1 = lista_de_1[k][0]
                v2 = lista_de_1[k][2]
                #print(f"\ni:{i} j:{j} l0:{v1} l2:{v2} sinal:{sinal}\n")
                if((int(v1) ==int(i)) and ((int(v2) == int(j)))):
                    #print("entrei")
                    sinal = 1
                    break
            if(sinal == 1):
                print(1,end=" ")
            else:
                print(0,end=" ")
            sinal =0

        print("]")


def Busca(elemento_procurado,fonte):
    #print(f"vou buscar {elemento_procurado}\nem\n{fonte}")
    try:
        val = fonte.index(elemento_procurado)
        #print(f"achei {val}\n")
    except:
        val = -1
        #print("não achei\n")
    return val
#Pega os vertices
while True:
    print("Digite o vertice do grafo :")
    temp = input()
    vertices.append(temp)
    if(temp == ""):
        vertices.pop(-1)
        break
#Pega as arestas
while True:
    print("Digite os dois vertices que compoem essa aresta do grafo no seguinte formado:\nv1 v2")
    temp = input()
    arestas.append(temp)
    if(temp == ""):
        arestas.pop(-1)
        break
print("Qual o nome desse Grafo ?")
nome_grafo = input()
print(f"{nome_grafo} = ({vertices}, {arestas})\n")

#impressao matriz de adjacencia vazia
linha = [0]*(len(vertices))
matriz_ad = [linha]*(len(vertices))
print(f"matriz de adjacencia a ser preenchida:\n{matriz_ad} \n\n")

def criador_da_lista_de_1(vertices,arestas)
    contador=0
    compoem_matriz_ad = []
    for i in vertices:
        for j in arestas:
            aux = j.split(" ")
            if(i == aux[0]):
                indice = Busca(aux[1],vertices)
                if(indice != -1):
                    x = f"{contador} {indice}"
                    print("x:")
                    print(x)
                    compoem_matriz_ad.append(x)
                elif(i == aux[1]):
                    indice = Busca(aux[0],vertices)
                    if(indice != -1):
                        x = f"{contador} {indice}"
                        print("x:")
                        print(x)
                        compoem_matriz_ad.append(x)
                        contador+=1
                        compoem_matriz_ad.sort()
                        return compoem_matriz_ad
imprime_matriz(compoem_matriz_ad,vertices)
