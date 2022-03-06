#Menu e criação grafo com teste criação matriz adjacencia - sem arquivo

i=0
def menu(i):

    #Finalização MENU por indecisão
    if(i == 3):
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
        vertices, arestas = cria_grafo(nome_grafo)
        print(f"{nome_grafo} = ({vertices}, {arestas})\n")

        menu(0)

    #Ler um grafo
    elif option == "B" or option == "b":
        #Abre um grafo
        print("Ok, digite o nome do grafo que você deseja carregar")
        menu(0)

    #Fechar Menu por opção
    elif option == "X" or option == "x":
        print("Aplicação será encerrada...")
        return 0

    #Testa estresse Menu
    else:
        print("Opção inválida!\nTente novamente.\n")
        i = i+1
        menu(i)


def cria_grafo(nome_grafo):
    vertices=[]
    arestas=[]
    #Pega os vertices
    while True:
        print("Digite o vertice do grafo (Se não houver digite ENTER):")
        temp = input()
        vertices.append(temp)
        if(temp == ""):
            vertices.pop(-1)
            break
            #Pega as arestas
    while True:
        print("Digite os dois vertices que compoem essa aresta do grafo no seguinte formato:  (Se não houver digite ENTER)\nv1 v2")
        temp = input()
        arestas.append(temp)
        if(temp == ""):
            arestas.pop(-1)
            break
    return vertices, arestas


#def cria_matriz_ad(G,V,E):
#    M = [None] * len(V)
#    for i in range(len(V)):
#        M[i] = [None] * len(V)
#        for j in range(len(V)):
#            M[i][j] = 0
#            for k in E:
#                if((k[0] == V[i] and k[1] == V[j]) or (k[0] == V[j] and k[1] == V[i])):
#                    M[i][j] = 1
#    print(f"print M: {M}\n")
#    return M

menu(0)
