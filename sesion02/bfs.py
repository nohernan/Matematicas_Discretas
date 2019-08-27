import queue
import graficas
from vertice import Vertice,Color

##########
## BFS
##########
def bfs(grafica, s):
    s.color = Color.gray
    s.distancia = 0
    s.padre = "nil"
    Q = queue.Queue()
    Q.put(s)
    
    while not(Q.empty()):
        u = Q.get()
        for v in grafica[u.nombre]:
            if v.color == Color.white:
                v.color = Color.gray
                v.distancia = u.distancia + 1
                v.padre = u.nombre
                Q.put(v)
        u.color = Color.black
                
bfs(graficas.g_bfs,graficas.bfs_s)

print ("\nDistancias calculadas")
for v in graficas.vertices_bfs:
    print ("Distancia a la raíz de ",v.nombre," es ",v.distancia)
    
    
print ("\nPadre dentro del árbol")
for v in graficas.vertices_bfs:
    print ("Padre del vertice ",v.nombre," es ",v.padre)

print ("\nColor de los vértices")
for v in graficas.vertices_bfs:
    print ("Color del vértice ",v.nombre," es ",v.color)
