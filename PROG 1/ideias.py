print("Oque deseja ?\nA) Criar um Grafo.\nB) Abrir um Grafo.")
option = input()
if option == "A" or option == "a":
    #Cria o Grafo
elif option == "B" or option == "b":
    #Abre um grafo
else:
    print("Opção inválida!")


print("Digite a quantidade de vertices do grafo :")
tamanho_v = input()
print("Digite a quantidade de arestas do grafo:")
tamanho_a = input()
vertices = []
arestas = []
#Aquisição Vertice e Arestas em serie
for i in range (1,tamanho_v) :
print(f"Informe o vertices {i} do grafo:")
vertices.append = input()

for i in range (1,tamanho_a) :
print(f"Informe a aresta {i} do grafo:")
vertices.append = input()

for i in range (1, tamanho_v):
    for j in range(1,tamanho_v):
        print(mat)
#Aquisição vertice e arestas string





for j in range(0,2):
val1 = i
val2 = j
print(f"\n{val1} i, {val2} j")
if(val1 == val2):
    matriz_ad[i][j] = 0
    print(f"{matriz_ad[i][j]}")
print("fim")
print(f"{matriz_ad} \n\n")


#___________________________________________________ FUNÇÕES PRONTAS

def menu(i):
    if(i == 3):
        print("Vejo que está indeciso, volte quando souber oque deseja.")
        return 0
    print("Oque deseja ?\nA) Criar um Grafo.\nB) Abrir um Grafo.\nX)Fechar.")
    option = input()
    if option == "A" or option == "a":
        #Cria o Grafo
        print("Ok vamos criar um grafo")
        cria_grafo()
        menu(0)
    elif option == "B" or option == "b":
        #Abre um grafo
        print("Ok, digite o nome do grafo que você deseja carregar")
        menu(0)
    elif option == "X" or option == "x":
        print("Aplicação será encerrada...")
        return 0
    else:
        print("Opção inválida!\nTente novamente.\n")
        i = i+1
        menu(i)


def cria_grafo():
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

def Busca(elemento_procurado,fonte):
    print(f"vou buscar {elemento_procurado}\nem\n{fonte}")
    try:
        val = fonte.index(elemento_procurado)
        print(f"achei {val}\n")
    except:
        val = -1
        print("não achei\n")
    return val
