# Una clase en Python para representar gráficas, mostrando
# aspectos y funcionalidades esenciales de las gráficas


class Graph(object):

    def __init__(self, graph_dict=None):
        # Si no se provee de un diccionario,
        # entonces se genera uno vacío
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        # Regresa los vértices de la gráfica
        return list(self.__graph_dict.keys())

    def edges(self):
        # Regresa los vértices de la gráfica
        return self.__generate_edges()

    def add_vertex(self, vertice):
        # Si 'vertice' no está en el diccionario de la gráfica,
        # ent. una llave con nombre 'vertice' y una lista vacía 
        # como valor se añade al diccionario.
        # Si 'vertice' ya forma parte del diccionario, no
        # se realiza ninguna acción
        if vertice not in self.__graph_dict:
            self.__graph_dict[vertice] = []

    def add_edge(self, arista):
        # Suponemos que  'arista' es de tipo tupla o lista
        (v1, v2) = tuple(arista)
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].append(v2)
        else:
            self.__graph_dict[v1] = [v2]

    def __generate_edges(self):
        # Un método estático generando las aristas del objecto 'graph'
        # que se pasó como argumento a la clase.
        aristas = []
        for v in self.__graph_dict:
            for ady in self.__graph_dict[v]:
                if (ady, v) not in aristas and (v, ady) not in aristas:
                    aristas.append((v, ady))
        return aristas

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\naristas: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)

    print("Vértices de la gráfica:")
    print(graph.vertices(),"\n")

    print("Aristas de la gráfica:")
    print(graph.edges(),"\n")

    print("Añadir un vértice:","\n")
    graph.add_vertex("z")

    print("Vértices de la gráfica :")
    print(graph.vertices(),"\n")
 
    print("Añadir una arista:","\n")
    graph.add_edge(("a","a"))
    
    print("Vértices de la gráfica:")
    print(graph.vertices(),"\n")

    print("Aristas de la gráfica:")
    print(graph.edges(),"\n")

    print('Añadir una arista ("x","y") con vértices nuevos:',"\n")
    graph.add_edge(("x","y"))
    
    print("Vértices de la gráfica:")
    print(graph.vertices(),"\n")
    
    print("Aristas de la gráfica:")
    print(graph.edges(),"\n")
  
