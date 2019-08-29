import enum

##############################
class Color(enum.Enum):
    white = 0
    gray = 1
    black = 2

##############################    
class Vertice:
    def __init__(self,nombre,color=Color.white,distancia="infinito",padre=None,descubierto=0,finalizado=0):
        self.__nombre = nombre

        self.__color = color
            
        self.__distancia = distancia
            
        self.__padre = padre

        ## DFS
        self.__descubierto = descubierto

        self.__finalizado = finalizado

    ## Get nombre
    @property
    def nombre(self):
        return self.__nombre

    ##
    ## Color
    ##
    ## Get color
    @property
    def color(self):
        return self.__color

    ## Set color
    @color.setter
    def color(self,c):
        self.__color = c

    ##
    ## Distancia
    ##
    ## Get distancia   
    @property
    def distancia(self):
        return self.__distancia

    ## Set distancia
    @distancia.setter
    def distancia(self,d):
        self.__distancia = d

    ##
    ## Padre
    ##
    ## Get padre
    @property
    def padre(self):
        return self.__padre

    ## Set padre
    @padre.setter
    def padre(self,p):
        self.__padre = p

    ##
    ## Descubierto
    ##
    ## Get descubierto       
    @property
    def descubierto(self):
        return self.__descubierto

    ## Set descubierto
    @descubierto.setter
    def descubierto(self,des):
        self.__descubierto = des

    ##
    ##  Finalizado
    ##
    ## Get finalizado       
    @property
    def finalizado(self):
        return self.__finalizado

    ## Set finalizado
    @finalizado.setter
    def finalizado(self,f):
        self.__finalizado = f

        
