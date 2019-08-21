import enum
import queue

##############################
class Color(enum.Enum):
    white = 0
    gray = 1
    black = 2

##############################    
class Vertice:
    def __init__(self,nombre,color=Color.white,distancia="infinito",padre=None):
        self.__nombre = nombre

        self.__color = color
            
        self.__distancia = distancia
            
        self.__padre = padre

    @property
    def nombre(self):
        return self.__nombre

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,c):
        self.__color = c


    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self,d):
        self.__distancia = d

    @property
    def padre(self):
        return self.__padre

    @padre.setter
    def padre(self,p):
        self.__padre = p


##############################
if __name__ == "__main__":

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
    
    
    bfs(g,v_c)

    print ("\nDistancias calculadas")
    for v in vertices:
        print ("Distancia a la raíz de ",v.nombre," es ",v.distancia)


    print ("\nPadre dentro del árbol")
    for v in vertices:
        print ("Padre del vertice ",v.nombre," es ",v.padre)

    print ("\nColor de los vértices")
    for v in vertices:
        print ("Color del vértice ",v.nombre," es ",v.color)


    
        
