import os
#PROGRAMA LEITOR/CRIADOR DE GRAFOS FEITO POR Alexandre Maia Martins Filho
def Busca(elemento_procurado,fonte):
    #print(f"vou buscar {elemento_procurado}\nem\n{fonte}")
    try:
        val = fonte.index(elemento_procurado)
        #print(f"achei {val}\n")
    except:
        val = -1
        #print("não achei\n")
    return val


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
    print()

def criador_da_lista_de_1(vertices,arestas):
    contador=0
    compoem_matriz_ad = []
    for i in vertices:
        for j in arestas:
            aux = j.split(" ")
            if(i == aux[0]):
                indice = Busca(aux[1],vertices)
                if(indice != -1):
                    x = f"{contador} {indice}"
                    #print("x:")
                    #print(x)
                    compoem_matriz_ad.append(x)
            elif(i == aux[1]):
                indice = Busca(aux[0],vertices)
                if(indice != -1):
                    x = f"{contador} {indice}"
                    #print("x:")
                    #print(x)
                    compoem_matriz_ad.append(x)
        contador+=1
    compoem_matriz_ad.sort()
    return compoem_matriz_ad

def busca_grafo(grafo_desejado):
    arquivo = open("grafos.ag","r")
    linha = arquivo.readline()
    while linha:
        nome = linha.split(" ")
        if(nome[0] == grafo_desejado):
            #print(f"Achei o {grafo_desejado} aqui {nome[0]}")
            arquivo.close()
            return 0
        linha = arquivo.readline()
    arquivo.close()
    return -1

def insere_grafo_arq(nome_grafo,vertices,arestas):
    arquivo =open("grafos.ag","a")
    arquivo.write(f"\n{nome_grafo} = ([")
    for i in range(len(vertices)):
        arquivo.write(vertices[i])
        if(i != (len(vertices)-1)):
            arquivo.write(" , ")
    arquivo.write("],[")
    for j in range(len(arestas)):
        arquivo.write(arestas[j])
        if(j != (len(arestas)-1)):
            arquivo.write(" , ")
    arquivo.write("])")
    arquivo.close()
    os.system('cls') or None
    print(f"Grafo inserido: {nome_grafo} = ({vertices}, {arestas})")

def cria_grafo(nome_grafo):
    vertices=[]
    arestas=[]
    #Pega os vertices
    print("Digite a quantidade de vertices do grafo (Se não houver digite ENTER):")
    n = int(input())
    print("Digite a quantidade de arestas do grafo (Se não houver digite ENTER):")
    m = int(input())


    for i in range(0,n):
        print(f"Digite o vertice {i} do grafo:")
        temp = input()
        vertices.append(temp)
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

def testa_arq():
    try:
        f = open("grafos.ag","r")
        print("iniciando aplicação\nBanco de Grafos encontrado.\n")
        f.close()
    except:
        f = open("grafos.ag","w")
        print("iniciando aplicação\nCriando Banco de grafos...\n")
        f.close()

def retorna_grafo(grafo_desejado):
    vertices = []
    arestas = []
    arquivo = open("grafos.ag","r")
    linha = arquivo.readline()
    while linha:
        nome = linha.split(" = ([")
        if(nome[0] == grafo_desejado):
            #print(f"Achei o {grafo_desejado} aqui {nome[0]}")
            #Código de aquisição lista vertices e arestas.
            pega = nome[1]
            V = pega.split("],[")
            V2 = V[0]
            A = V[1]
            A2 = A.split(" , ")
            limite = len(A2)
            A3 = A2[limite-1]
            A2.pop(-1)
            arestas = A2
            A4 = A3.split("])\n")
            arestas.append(A4[0])
            vertices = V2.split(" , ")
        linha = arquivo.readline()
    arquivo.close()
    return vertices, arestas

def menu(i):
    #Criação ou Leitura arquivo com Grafos.
    testa_arq()
    #Finalização MENU por indecisão
    if(i == 3):
        os.system('cls') or None
        print("Vejo que está indeciso, volte quando souber oque deseja.")
        return 0

    #Inicio Menu
    print("Oque deseja ?\nA) Criar um Grafo.\nB) Abrir um Grafo.\nX)Fechar.")
    option = input()

    #Criar um Grafo
    if option == "A" or option == "a":
        #Cria o Grafo
        print("Ok vamos criar um grafo")
        print("Qual o nome desse Grafo ?")
        nome_grafo = input()
        vertices=[]
        arestas=[]
        lista_1=[]
        if(busca_grafo(nome_grafo) != -1):
            os.system('cls') or None
            print("\nGrafo ja existente. Tente outro nome na proxima.\n")
        else:
            vertices, arestas = cria_grafo(nome_grafo)
            insere_grafo_arq(nome_grafo,vertices,arestas)
            lista_1 = criador_da_lista_de_1(vertices,arestas)
            imprime_matriz(lista_1,vertices)
        menu(0)

    #Ler um grafo
    elif option == "B" or option == "b":
        #Abre um grafo
        print("Ok\n Qual o nome desse Grafo que você deseja carregar ?")
        nome_grafo = input()
        vertices=[]
        arestas=[]
        lista_1=[]
        if(busca_grafo(nome_grafo) != -1):
            #vertices, arestas = retorna_grafo(nome_grafo)
            vertices, arestas = retorna_grafo(nome_grafo)
            os.system('cls') or None
            print(f"{nome_grafo} = ({vertices}, {arestas})\n")
            lista_1 = criador_da_lista_de_1(vertices,arestas)
            imprime_matriz(lista_1,vertices)
        else:
            os.system('cls') or None
            print("\nGrafo não existe. Tente outro nome na proxima.\n")
        menu(0)

    #Fechar Menu por opção
    elif option == "X" or option == "x":
        print("Aplicação será encerrada...")
        return 0

    #Testa estresse Menu
    else:
        os.system('cls') or None
        print("\nOpção inválida!\nTente novamente.\n")
        i = i+1
        menu(i)

os.system('cls') or None
menu(0)
