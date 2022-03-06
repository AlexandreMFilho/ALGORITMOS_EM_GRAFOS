#Cria a  grafo, tudo certo exceto a parte da matriz de adjacencia

def imprime_matriz(lista_de_1,n):
    print(lista_de_1)
    limite=len(n)
    for i in range(0,limite):
        #print("[",end=" ")
        for j in range(0,limite):
            sinal =0
            for k in lista_de_1:
                v1=Busca(i,k)
                v2=Busca(j,k)
            if(v1 != -1 and v2 != -1):
                    sinal = 1
                    print(1,end=" ")
            if(sinal ==1 ):
                print(1,end=" ")
            else:
                print(0,end=" ")



#
#            for k in lista_de_1:
#                aux = k.split(" ")
#                sinal = 0
#                v1 = aux[0]
#                v2 = aux[1]
#                print(f"\naux:{aux} i:{i} j:{j}\n")
#                if(i == v1 and j == v2):
#                    print("eh igual\n")
#                    sinal = 1
#                    break
#                print(f"sin:{sinal}")
#        if (sinal == 1):
#            print(1, end=" ")
#        else:
#            print(0,end=" ")
        #print("]")
#
#    for k in lista_de_1:
#        aux = k.split(" ")
#        for i in range(0,len(vertices)):
#            for j in range(0,len(vertices)):
#                Busca(i,aux[0])
#                print(f"a[0]:{aux[0]} a[1]:{aux[1]}")
#                print(f"i:{i} j:{j}")
#                if(i == aux[0] and j == aux[1]):
#                    print(1)
#                    break
#                else:
#                    print(0)
#                    break
#        print()
#    print()

def Busca(elemento_procurado,fonte):
    #print(f"vou buscar {elemento_procurado}\nem\n{fonte}")
    try:
        val = fonte.index(elemento_procurado)
        #print(f"achei {val}\n")
    except:
        val = -1
        #print("não achei\n")
    return val

vertices=[]
arestas=[]
matriz_ad=[]

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
imprime_matriz(compoem_matriz_ad,vertices)
#separador=[]
#for i in arestas:
#    separador = i.split(" ")
#    v1 = Busca(separador[0],vertices)
#    v2 = Busca(separador[1],vertices)
#    for i in matriz_ad:
#        for j in i:
            #if(i == v1 and j == v2):
#            i[j] = 1

#    if(v1 != -1 and v2 != -1):
#        print(f"essa aresta existe, então vou marcar os índices {v1}x{v2} e {v2}x{v1} da matriz.\n")
#        print(f"v1v2:{matriz_ad[v1][v2]}")
#        print(f"v2v1:{matriz_ad[v2][v1]}")
#        print(f"{matriz_ad} \n\n")

#        matriz_ad[v1][v2] = 1
#        matriz_ad[v2][v1] = 1

#        print(f"v1v2:{matriz_ad[v1][v2]}")
#        print(f"v2v1:{matriz_ad[v2][v1]}")
#        print(f"{matriz_ad} \n\n")


#print(f"{matriz_ad} \n\n")
