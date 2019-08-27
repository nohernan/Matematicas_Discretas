import queue
import graficas
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
    u.descubierto = time
    u.color = Color.gray
    for v in grafica[u.nombre]:
        if v.color == Color.white:
            v.padre = u.nombre
            dfs_visit(grafica,v)
    u.color = Color.black
    time += 1
    u.finalizado = time
    
                
dfs(graficas.g_dfs,graficas.vertices_dfs)

print ("\nTiempos de descubrimiento y de término")
for v in graficas.vertices_dfs:
    print ("Tiempo en el que el vértice ",v.nombre," es descubierto ",v.descubierto)
    print ("Tiempo en el que el vértice ",v.nombre," se termina de analizar ",v.finalizado,"\n")
    
    
print ("\nPadre dentro del árbol")
for v in graficas.vertices_dfs:
    print ("Padre del vertice ",v.nombre," es ",v.padre)

