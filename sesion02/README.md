# Sesión 2

## Actividades programadas:

* Programación de estructuras recursivas.
* Representación de gráficas.
* Árboles.

---

## Programación de estructuras recursivas en Haskell

En el archivo [estruc_rec.hs](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/estruc_rec.hs) se encuentran definidas de manera recursiva las fórmulas de la lógica proposicional, las listas de elementos de tipo `a` y los árboles binarios con elementos de tipo `a`.

---

## Representación de gráficas en Python

Una buena parte del contenido que se muestra enseguida fue tomado de [este enlace](https://www.python-course.eu/graphs_python.php).

Python no tiene un tipo de datos integrado para gráficas, pero es fácil implementarlas en Python. Un tipo de datos es ideal para representar gráficas en Python, los [diccionarios](https://www.python-course.eu/dictionaries.php). Considere la siguiente gráfica


Puede ser implementada en Python de la siguiente manera

```python
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
```
Las llaves del dictionario son los vértices de nuestra gráfica. Los valores correspondientes son listas de adyacencia para el vértice en cuestión.

A continuación se muestra una función que lista todas las aristas de la gráfica:

```python
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

print(generate_edges(graph))
```

Como resultado de ejecutar el código anterior sobre el dictionario arriba dado, ambas presentes en el archvo, obteniendo como salida:

```python
$ python3 graph_simple.py 
[('a', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('b', 'c'), ('b', 'e'), ('e', 'c'), ('e', 'b'), ('d', 'c')]
```

### Gráficas como una clase de Python