import enum

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
