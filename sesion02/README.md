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

Python no tiene un tipo de datos integrado para gráficas, pero es fácil implementarlas en Python. Los [diccionarios](https://www.python-course.eu/dictionaries.php) son un tipo de datos ideal para representar gráficas en Python. Considere la siguiente gráfica

![diagrama0](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/img/diagram0.png "Diagrama inicial")

Puede ser implementada en Python de la siguiente manera

```python
mi_grafica = { "a" : ["b", "c","d"],
               "b" : ["a", "c"],
               "c" : ["a", "b"],
               "d" : ["a"],
               "e" : []
              }
```
Las llaves del dictionario son los vértices de nuestra gráfica. Los valores correspondientes son listas de adyacencia para el vértice en cuestión.

A continuación se muestra una función que lista todas las aristas de la gráfica:

```python
def generar_aristas(grafica):
    aristas = []
    for v in grafica:
        for adyacente in grafica[v]:
            aristas.append((v, adyacente))

    return aristas

print(generar_aristas(mi_grafica))
```

Como resultado de ejecutar el código anterior sobre el diccionario arriba dado, ambos presentes en [rep_graf.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/rep_graf.py), mediante el comando `$ python3.7 rep_graf.py` obtenemos:

```python
[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('d', 'a')]
```

### Gráficas como una clase de Python

Para mayor información y explicación sobre la orientación a objetos en _Python_ se pueden consultar las siguientes ligas:
1. [Documentación oficial](https://docs.python.org/3/tutorial/classes.html).
1. [Course sobre _Python_](https://www.python-course.eu/python3_object_oriented_programming.php).
1. [Real python](https://realpython.com/python3-object-oriented-programming/).
1. [Programiz](https://www.programiz.com/python-programming/object-oriented-programming).

En el archivo [clase_graficas.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/clase_graficas.py) se tiene una clase que representa gráficas. Al ejecutarla se imprime en pantalla los elementos de la gráfica que se muestra abajo. También se ejemplifica como es que se añaden vértices y aristas.

![diagrama1](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/img/diagram1.png "Diagrama Dos")


### BFS en Python
El algortimo que hace búsqueda por amplitud en gráficas se encuentra en [bfs.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/bfs.py) y se ejecuta sobre la gráfica anterior.

