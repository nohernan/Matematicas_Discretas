# Sesión 1

## Actividades programadas:

* Introducción a Python.
* Programación de números naturales.
* Programación de sucesión de Fibonacci y número de Perrín.
* Recursión.

---

# Haskell

Algunas características y funcionalidad básica de _haskell_ se puede apreciar en el archivo [primeros_pasos.hs](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/primeros_pasos.hs). Allí se ejemplifican
1. la definición de funciones,
1. la composición de funciones,
1. el uso de `let` y `where`,
1. las funciones anónimas, y
1. las listas por comprensión.

### Ejercicio
Programar en _haskell_ una función `elem_maximo(lst)` que encuentre el elemento máximo en la lista `lst` de enteros no negativos.

---

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

Una lista del factorial de los números del 0 al 99 (y también del 999) [aquí](http://www.tsm-resources.com/alists/fact.html).

**Fibonacci**

* `*Main> fib 28`
* `*Main> fib 38`
* `*Main> fib (-35)`

Una lista ahora de la serie de Fibonacci de los números del 0 al 300 [acá](http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html).

Desde el intérprete de _haskell_ se genera una lista con los primeros 30 números de Fibonacci del siguiente modo, nótese el uso de listas por comprensión.

`*Main> [fib(n) | n <-[0..30]]`


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

## Rango

La función `range()` produce una lista de números sobre la que típicamente se itera mediante _loops_. A menudo se requiere este uso cuando se realiza una cierta acción por un número determinado de veces, prestanto atención o no al índice que se va generando. En otras ocasiones se requiere iterar sobre una lista tomando en cuenta el índice generado.

La función `range()` puede ser llamada de dos maneras:

1. `range(stop)` donde `stop` representa el número de enteros a generar, comenzando en cero. Por  ejemplo, `range(3) = [0,1,2]`.
1. `range([start,] stop[, step])`
    1. `start`: valor inicial de la lista.
    1. `stop`: se generan todos los números posibles iniciando en `start` con una diferencia de `step` sin rebasar a `stop` ni igualarlo.
    1. `step`: diferencia entre cada número en la lista.

Obsérvese que:
* Todos los parámetros deben ser enteros.
* Todos los parámetros pueden ser positivos o negativos.
* `range()` está basado en el índice 0, es decir, los índices de las listas inician en 0, no en 1. La sintaxis para accesar al primer elemento de una lista es `lista[0]`. Por lo tanto, el último entero generado por `range()` es el número más cercano a `stop`, distinto de él y sin rebasarlo, iniciando en `start` con una diferencia de `step` a cada instante. Por ejemplo, `range(1,5)` produce la lista `[1,2,3,4]` y `range(10,3,-2)` a la lista `[10,8,6,4]`.

Más información en [este enlace](https://www.pythoncentral.io/pythons-range-function-explained/).

## Indexación

Se pueden extraer secciones de arreglos mediante indexación usando la sintaxis estándar de Python. Tales reglas de sintaxis incluyen los siguientes casos:

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

### Ejercicio

Usted tiene una cantidad específica de dinero en su cuenta de banco. Cada año su saldo incrementa a la misma `taza` de interés. Suponiendo que usted no retira ni hace depósitos adicionales, determine cuanto tiempo se requiere para sobrepasar un `umbral` específico. 

La firma de la función a implementar debe ser `depositProfit(deposito, taza, umbral)`.

#### Ejemplo de ejecución

Para `deposito = 100`, `taza = 20` y `umbral = 170`, la salida debe ser `depositProfit(deposito, taza, umbral) = 3`.

---

Más ejemplos de funciones recursivas definidas en Python se encuentran en el archivo [recursion.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/recursion.py), donde se estudian el factorial, la serie de Fibonacci y la serie de [Perrin](http://mathworld.wolfram.com/PerrinSequence.html). Para ejecutar los ejemplos en dicho archivo empleamos la instrucción siguiente en una terminal con directorio actual de trabajo `Matematicas_Discretas/sesion01/`.

`$ python 3.7 recursion.py`

---

En clases posteriores se estudiará la complejidad de los algoritmos. En particular, se verá como es su desempeño en términos de una familia de funciones que tiene un mismo comportamiento. Por ejemplo, una familia de funciones para el logaritmo tiene asociadas varias funciones logaritmo con distintas bases, pero dada la fórmula

![equation](https://latex.codecogs.com/gif.latex?log_a%28x%29%3D%5Cfrac%7Blog_b%28x%29%7D%7Blog_b%28a%29%7D) 

sabemos que los elementos de tal familia varían por un factor contante, es decir, son linealmente dependientes. Para graficar el logaritmo en varias bases consideramos el archivo [plot_log.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/plot_log.py). Para ejecutar dicho archivo tenemos que instalar algunas bibliotecas de Python con los comandos:

1. `$ sudo apt-get install python-pip python3.7-pip`
1. `$ sudo pip3.7 install --upgrade pip`
1. `$ sudo -H pip3.7 install -U numpy`
1. `$ sudo -H pip3.7 install -U matplotlib`

Ahora sí podemos correr la siguiente instrucción en una terminal abierta en la misma ubicación donde está `plot_log.py`.

`$ python3.7 plot_log.py`

