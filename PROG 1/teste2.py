#Usar para tentar ler e armazenar os grafos do arquivo
#Um teste onde consegui criar e adicionar texto a um arquivo, formatação do grafo OK
#CONSEGUI CARREGAR OS VERTICES E ARESTAS DO GRAFO GOD D+
def busca_grafo(grafo_desejado):
    arquivo = open("grafos.ag","r")
    linha = arquivo.readline()
    while linha:
        nome = linha.split(" ")
        if(nome[0] == grafo_desejado):
            print(f"Achei o {grafo_desejado} aqui {nome[0]}")
            arquivo.close()
            return 0
        linha = arquivo.readline()
    arquivo.close()
    return -1

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
try:
    f = open("grafos.ag","r")
    print("Banco de Grafos encontrado.\n")
    f.close()
except:
    f = open("grafos.ag","w")
    print("Criando Banco de grafos...\n")
    f.close()

print("Qual o nome desse Grafo ?")
nome_grafo = input()
vertices=[]
arestas=[]
if(busca_grafo(nome_grafo) != -1):
    vertices, arestas = retorna_grafo(nome_grafo)
    print(f"{nome_grafo} = ({vertices}, {arestas})\n")
else:
    print("Grafo não existe.")
