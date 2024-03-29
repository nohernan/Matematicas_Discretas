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

#### Propiedades
La búsqueda por amplitud encuentra en la gráfica G las distancias más cortas para las trayectorias que llegan a cada vértice desde un vértice origen _s_. La distancia más corta para la trayectoria de _s_ a _v_ es el mínimo número de aristas en cualquier trayectoria que parta del vértice _s_ y que llegue a _v_; si no hay trayectoria de _s_ a _v_, entonces la distancia más corta para la trayectoria de _s_ a _v_ es infinito. El prodecimiento de búsqueda por amplitud construye un árbol por amplitud al ir analizando la gráfica G. Este árbol se forma con los atributos _padre_ de los vértices, por lo que la llamamos subgráfica de predecesores de G. El árbol por amplitud contiene una trayectoria única simple de _s_ a _v_ que es también la trayectoria más corta de _s_ a _v_ en G.

#### Ejercicio
El diámetro de un árbol T=(V,E) se define como la distancia más grande de entre las trayectorias más cortas para el árbol. Proporcione un algoritmo para calcular el diámetro de un árbol.

#### Aplicación
Supongamos que de entrada tenemos una gráfica _G = (V, E)_, representando una matriz _M_ de _nxn_ elementos. ¿Qué permutación de los vértices de _V_ minimiza la longitud de la arista más grande cuando los vértices se ordenan sobre una línea? Este problema se conoce como _reducción del ancho de banda_ y surge, por ejemplo, al acomodar un conjunto de _n_ componentes de un circuito en línea sobre una placa de manera que se minimice la longitud del cable más largo, donde podemos considerar a cada componente del circuito como un vértice y a cada cable enlazando a dos componentes como una arista. Alternativamente, considere una aplicación de hipertexto de manera que se almacenan objetos grandes (como imágenes) en una cinta magnética. De cada imagen hay un conjunto de posibles imágenes a las que se pueden llegar (i.e. los hipervínculos). Para minimizar el tiempo de búsqueda, se intenta acomodar imágenes enlazadas cerca una de la otra en la cinta. Este es justamente el problema de reducción de ancho de banda.

Hay heurísticas que se basan en ejecutar una búsqueda primero por amplitud desde un vértice dado _v_, donde _v_ se ubica en el punto más a la izquierda. Todos los vértices a distancia 1 de _v_ se ubican a su derecha inmediata, seguidos por lo vértices a distancia 2, así se continúa hasta llegar al vértice más alejado de _v_.

---

### DFS en Python
El algortimo que hace búsqueda por amplitud en gráficas se encuentra en [bfs.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/bfs.py), su ejecución se ejemplifica por la imagen siguiente, tomada del libro _Introduction to Algorithms_ por Thomas H. Cormen, et al.

![dfs](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion02/img/dfs.png "DFS")

#### Propiedades de la búsqueda a profundidad
La búsqueda a profundidad produce información valiosa acerca de la estructura de la gráfica. La propiedad básica más importante es que la subgráfica de predecesores forma un bosque de árboles. Otra propiedad importante de esta búsqueda es que los tiempos en los que los vértices son descubiertos y finalizados tienen una ***estructura de paréntesis***. Si representamos el descubrimiento de un vértice _u_ con un paréntesis izquierdo "_(u_" y representamos su término por un paréntesis derecho "_u)_", entonces la historia de descubrimientos y términos genera una expresión bien formada en el sentido de que los paréntesis están anidados apropiadamente.

#### Ejercicios
1. Reescriba el procedimiento DFS, usando una pila para eliminar la recusión.
1. Muestre que podemos usar una búsqueda a profundidad sobre una gráfica no dirigida G para identifiar las componentes conexas de G, y que el bosque a profundidad contiene tantos árboles como G tiene componentes conexas. Es decir, muestre como modificar la búsqueda a profundidad para asignar a cada vértice _v_ un entero _v.cc_ entre 1 y _k_, donde _k_ es el número de componentes conexas de G, tal que _u.cc_ = _v.cc_ si y solo si _u_ y _v_ estań en la misma componente conexa.
1. Proporcione un algoritmo que decida si una gráfica no dirigida G=(V,E) contiene un ciclo. 


#### Aplicación
Supongamos que se tiene una gráfica _G=(V,E)_. Deseamos colorear los vértices de _V_ usando el mínimo número de colores tal que para cada arista _(i,j)_, los vértices _i_ y _j_ tienen diferentes colores. ¿Se puede colorear la gráfica usando únicamente dos diferentes colores? - Un caso especial importante es determinar si una gráfica es _bipartita_, lo que significa que puede ser coloreada usando dos colores diferentes. Tal coloración de los vértices de una gráfica bipartita significa que la gráfica puede ser dibujada con vértices rojos a la izquierda y azules a la derecha de manera que todas las aristas van de izquierda a derecha. Las gráficas bipartitas surgen naturalmente en aplicaciones tales como la asignación de posibles tareas a trabajadores.

Verificar si una gráfica es bipartita es fácil. Se colorea el primer vértice azul, se realiza entonces una búsqueda a profundidad sobre la gráfica. Cada que se descubre un vértice nuevo sin color, se pinta opuesto a su padre. Si en algún momento se encuentra una arista con ambos vértices del mismo color, entonces la gráfica no puede ser bipartita. De otro modo, esta coloración será exitosa usando únicamente dos colores.