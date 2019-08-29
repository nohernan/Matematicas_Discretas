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

#### Ejercicio
La transpuesta de una gráfica dirigida G=(V,E) es la gráfica Gt=(V,Et), donde Et = {(_v_,_u_)<-V x V | (_u_,_v_)<-E}. Así, Gt es G con todas sus aristas revertidas. Describa un algoritmo para calcular Gt a partir de G, para la representación de G por listas de adjacencia y por matriz de adyacencia. 

### Gráficas como una clase de Python

Para mayor información y explicación sobre la orientación a objetos en _Python_ se pueden consultar las siguientes ligas:
1. [Documentación oficial](https://docs.python.org/3/tutorial/classes.html).
1. [Course sobre _Python_](https://www.python-course.eu/python3_object_oriented_programming.php).
1. [Real python](https://realpython.com/python3-object-oriented-programming/).
1. [Programiz](https://www.programiz.com/python-programming/object-oriented-programming).

En el archivo [clase_graficas.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/clase_graficas.py) se tiene una clase que representa gráficas. Al ejecutarla se imprime en pantalla los elementos de la gráfica que se muestra abajo. También se ejemplifica como es que se añaden vértices y aristas.

![diagrama1](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/img/diagram1.png "Diagrama Dos")


### BFS en Python
El algortimo que hace búsqueda por amplitud en gráficas se encuentra en [bfs.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/bfs.py), su ejecución se ejemplifica por la imagen siguiente, tomada del libro _Introduction to Algorithms_ por Thomas H. Cormen, et al.

![bfs](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/img/bfs.png "BFS")


### DFS en Python
El algortimo que hace búsqueda por amplitud en gráficas se encuentra en [bfs.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/bfs.py), su ejecución se ejemplifica por la imagen siguiente, tomada del libro _Introduction to Algorithms_ por Thomas H. Cormen, et al.

![dfs](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/img/dfs.png "DFS")

#### Ejercicios
1. Reescriba el procedimiento DFS, usando una pila para eliminar la recusión.
1. Muestre que podemos usar una búsqueda a profundidad sobre una gráfica no dirigida G para identifiar las componentes conexas de G, y que el bosque a profundidad contiene tantos árboles como G tiene componentes conexas. Es decir, muestre como modificar la búsuqeda a profundidad para asignar a cada vértice _v_ un entero _v.cc_ entre 1 y _k_, donde _k_ es el número de componentes conexas de G, tal que _u.cc_ = _v.cc_ si y solo si _u_ y _v_ estań en la misma componente conexa.
