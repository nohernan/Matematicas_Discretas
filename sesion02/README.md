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

Como resultado de ejecutar el código anterior sobre el dictionario arriba dado, ambas presentes en el archivo [rep_graf.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/rep_graf.py), obtenemos como salida:

```python
$ python3.7 rep_graf.py
[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('d', 'a')]
```

### Gráficas como una clase de Python