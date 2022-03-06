#Um teste onde consegui criar e adicionar texto a um arquivo, formatação do grafo OK

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


try:
    f = open("grafos.ag","r")
    print("Banco de Grafos encontrado.\n")
    f.close()
except:
    f = open("grafos.ag","w")
    print("Criando Banco de grafos...\n")
    f.close()

f = open("grafos.ag","a")

print("Qual o nome desse Grafo ?")
nome_grafo = input()
vertices=[]
arestas=[]
vertices, arestas = cria_grafo(nome_grafo)
f.write(f"\n{nome_grafo} = ([")
for i in range(len(vertices)):
    f.write(vertices[i])
    if(i != (len(vertices)-1)):
        f.write(" , ")
f.write("],[")
for j in range(len(arestas)):
    f.write(arestas[j])
    if(j != (len(arestas)-1)):
        f.write(" , ")
f.write("])")
print(f"{nome_grafo} = ({vertices}, {arestas})\n")
