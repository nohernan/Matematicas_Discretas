# Sesión 1

## Actividades programadas:

* Introducción a Python.
* Programación de números naturales.
* Programación de sucesión de Fibonacci y número de Perrín.
* Recursión.

---

# Haskell

En el archivo [recursion.hs](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/recursion.hs) se encuentran algunas definiciones y funciones recursivas descritas en el lenguaje _haskell_.

En una terminal con directorio actual de trabajo `Matematicas_Discretas/sesion01/` se ejecuta la siguiente instrucción para llamar al intérprete de _haskell_:

`$ stack ghci`

Enseguida se carga el archivo `recursion.hs` mediante el comando:

```haskell
Prelude> :l recursion.hs
```

## Ejemplo de ejecución en haskell

**Operaciones en número naturales.**

* Suma: `*Main> sumNat (S Z) (S (S Z))`
* Multiplicación: `*Main> multNat (S (S Z)) (S (S (S (S Z))))`

**Factorial**

* `*Main> fact 20`
* `*Main> fact 5467`
* `*Main> fact (-7)`

Una [lista](http://www.tsm-resources.com/alists/fact.html) del factorial de los números del 0 al 99 (y también del 999).

**Fibonacci**

* `*Main> fib 28`
* `*Main> fib 38`
* `*Main> fib (-35)`

Una [lista](http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html) ahora de la serie de Fibonacci de los números del 0 al 300.

---

# Python

## Arreglos

Una de las estructuras de datos más fundamentales en cualquier lenguaje de programación son los arreglos. Python no tiene una estructura de datos de arreglos nativos, pero tiene listas que son más generales y pueden ser usadas como arreglos multidimensionales muy fácilmente. Una lista es un colección ordenada de objetos de cualquier tipo.

## Cadenas

Python tiene un clase de cadenas (_strings_) integrada llamada "str" con muchas caracterísitcas útiles. Las literales de tipo cadenas pueden ser delimitadas por comillas dobles o sencillas, aunque las comillas simples son usadas más comúnmente. La diagonal invertida escapa símbolos de la forma habitual dentro de las comillas dobles o senciilas -- por ejemplo \n \\' \\". Las cadenas en Python son "inmutables" lo que significa que no pueden cambiar después de que han sido creadas. Carácteres en una cadena pueden ser accesados usando las sintaxis estándar [ ], y como Java o C++, Python usa un sistema de índices base cero, de modo que si _s_ es 'hola' _s[1]_ es 'o'.

## Listas por comprensión

Las listas por comprensión proveen de una menara concisa para crear listas. Entre las aplicaciones más comunes se encuentran la generación de nuevas listas donde cada elemento es el resultado de aplicar algunas operaciones a cada miembro de otra secuencia, o para crear una subsecuencia de los elementos que satisfacen cierta condición.

Por ejemplo, supongamos que queremos crear una lista de cuadrados de números, el siguiente código realiza la tarea de forma elegante y breve:

```python
squares = [x**2 for x in range(10)]
```

Una lista por comprensión consiste de corchetes conteniendo una expresión seguida de una cláusula _for_, seguida de cero o más cláusulas _for_ o _if_. El resultado será una nueva lista que se obtiene de evaluar la expresión en el contexto de las cláusulas _for_ of _if_ que siguen. Por ejemplo, la lista que se define abajo combina elementos de dos lsitas si es que no son iguales:

```python
>>>
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

## Indexación

Los arreglos pueden ser indexados usando la sintexis estándar de Python. Tales reglas de sintaxis incluyen los siguientes casos:

```python
a[start:stop]  # elementos comenzando en start hasta stop-1
a[start:]      # elementos comenzando en start hasta el final del arreglo
a[:stop]       # elementos desde el inicio hasta stop-1
a[:]           # copia el arreglo completo
```

Hay también un valor de escalonamiento, el cual puede ser combinado con la sintaxis que se acaba de describir del siguiente modo: 


```python
a[start:stop:step] # elementos comenzando en start no rebasando a stop, con un escalonamiento de step
```

El punto clave es recordar que el valor `:stop` representa el primer valor que no pertenece a la rebanada que se está determinando. Así, la diferencia entre `stop` y `start` es el número de elementos seleccionados (si es que `step` es 1, el valor por defecto).

Más información sobre la indexación en este [link](https://stackoverflow.com/questions/509211/understanding-slice-notation).

---

En el archivo [intro.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/intro.py) se tienen definidas algunas funciones en Python que utilizan los elementos anteriormente definidos.

* La función _adjacentElementsProducts_ encuentra un par de elementos adjuntos de un arreglo de enteros tales que su multiplicación es la mayor posible, y regresa tal multiplicación.
* La función _allLongestStrings_ regresa un arreglo conteniendo todas las cadenas más grandes pertenecientes al arreglo que se le pasa como argumento.
* La función _alternatingSums_ toma como argumento un arreglo de enteros positivos _A_ y regresa un arreglo de dos enteros, donde el primero es la suma total de los números en posiciones pares en _A_ y el segundo es la suma total de los números en posiciones impares en _A_.
* La función _alternatingSums\_rec_ es la versión recursiva de _alternatingSums_.

Las funciones aquí descritas se tomaron de [https://codesignal.com/](https://codesignal.com/).

Para ejecutar el archivo abrimos una terminal con directorio actual de trabajo `Matematicas_Discretas/sesion01/`. Enseguida corremos la instrucción 

`$ python 3.7 intro.py`

---

Más ejemplos de funciones recursivas definidas en Python se encuentran en el archivo [recursion.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/recursion.py), donde se estudian el factorial, la serie de Fibonacci y la serie de [Perrin](http://mathworld.wolfram.com/PerrinSequence.html). Para ejecutar los ejemplos en dicho archivo empleamos la instrucción siguiente en una terminal con directorio actual de trabajo `Matematicas_Discretas/sesion01/`.

`$ python 3.7 recursion.py`

---

En clases posteriores se estudiará la complejidad de los algoritmos. En particular, se verá como es su desempeño en términos de una familia de funciones que tiene un mismo comportamiento. Por ejemplo, una familia de funciones para el logaritmo tiene asociadas varias funciones logaritmo con distintas bases, pero dada la fórmula

![equation](https://latex.codecogs.com/gif.latex?log_a%28x%29%3D%5Cfrac%7Blog_b%28x%29%7D%7Blog_b%28a%29%7D) 

sabemos que los elementos de tal familia varían por un factor contante. Para graficar el logaritmo en varias bases consideramos el archivo [plot_log.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/plot_log.py). Para ejecutar dicho archivo tenemos que instalar algunas bibliotecas de Python con los comandos:

1. `$ sudo apt-get install python-pip python3.7-pip`
1. `$ sudo pip3.7 install --upgrade pip`
1. `$ sudo -H pip3.7 install -U numpy`
1. `$ sudo -H pip3.7 install -U matplotlib`

Ahora sí podemos correr la siguiente instrucción en una terminal abierta en la misma ubicación donde está `plot_log.py`.

`$ python3.7 plot_log.py`

