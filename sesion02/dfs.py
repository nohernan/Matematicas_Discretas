import queue
from vertice import Vertice,Color

##########
## DFS
##########
time = 0

def dfs(grafica, vertices):
    for u in vertices:
        if u.color == Color.white:
            dfs_visit(grafica,u)

def dfs_visit(grafica,u):
    global time
    time += 1
    u.distancia = time
    u.color = Color.gray
    for v in grafica[u.nombre]:
        if v.color == Color.white:
            v.padre = u.nombre
            dfs_visit(grafica,v)
    u.color = Color.black
    time += 1
    
                
##############################
v_a = Vertice("a")
v_b = Vertice("b")
v_c = Vertice("c")
v_d = Vertice("d")
v_e = Vertice("e")
v_f = Vertice("f")

vertices = [v_a, v_b, v_c, v_d, v_e, v_f]
    
g = { "a" : [v_d],
      "b" : [v_c],
      "c" : [v_b, v_c, v_d, v_e],
      "d" : [v_a, v_c],
      "e" : [v_c],
      "f" : []
}


dfs(g,vertices)

#print ("\nDistancias calculadas")
#for v in vertices:
#    print ("Distancia a la raíz de ",v.nombre," es ",v.distancia)
    
    
print ("\nPadre dentro del árbol")
for v in vertices:
    print ("Padre del vertice ",v.nombre," es ",v.padre)

#print ("\nColor de los vértices")
#for v in vertices:
#    print ("Color del vértice ",v.nombre," es ",v.color)
