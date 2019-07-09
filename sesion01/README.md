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

`Prelude> :l recursion.hs`

## Ejemplo de ejecución en haskell

**Operaciones en número naturales.**

* Suma: `*Main> sumNat (S Z) (S (S Z))`
* Multiplicación: `*Main> multNat (S (S Z)) (S (S (S (S Z))))`

**Factorial**

* `*Main> fact 20`
* `*Main> fact 5467`
* `*Main> fact (-7)`

Una [lista](http://www.tsm-resources.com/alists/fact.html) del factorial de los números del 0 al 69.

**Fibonacci**

* `*Main> fib 28`
* `*Main> fib 38`
* `*Main> fib (-35)`

---

# Python

## Arreglos

Una de las estructuras de datos más fundamentales en cualquier lenguaje de programación son los arreglos. Python no tiene una estructura de datos de arreglos nativos, pero tiene listas que son más generales y pueden ser usadas como arreglos multidimensionales muy fácilmente. Una lista es un colección ordenada de objetos de cualquier tipo.

## Strings

Python tiene un clase de cadenas (_strings_) integrada llamada "str" con muchas caracterísitcas útiles. Las literales de tipo cadenas pueden ser delimitadas por comillas dobles o sencillas, aunque las comillas simples son usadas más comúnmente. La diagonal invertida escapa símbolos de la forma habitual dentro de las comillas dobles o senciilas -- por ejemplo \n \\' \\". Las cadenas en Python son "inmutables" lo que significa que no pueden cambiar después de que han sido creadas. Carácteres en una cadena pueden ser accesados usando las sintaxis estándar [], y como Java o C++, Python usa un sistema de índices base cero, de modo que si _s_ es 'hola' _s[1]_ es 'o'.

En el archivo [intro.py](https://github.com/nohernan/Matematicas_Discretas/blob/master/sesion01/intro.py) se tienen definidas algunas funciones en Python que utilizan los elementos anteriormente definidos.

* La función _adjacentElementsProducts_ encuentra un par de elementos adjuntos de un arreglo de enteros tales que su multiplicación es la mayor posible, y regresa tal multiplicación.
* La función _allLongestStrings_ regresa un arreglo conteniendo todas las cadenas más grandes pertenecientes al arreglo que se le pasa como argumento.

Las funciones aquí descritas se tomaron de [https://codesignal.com/](https://codesignal.com/).

Para ejecutar el archivo abrimos una terminal con directorio actual de trabajo `Matematicas_Discretas/sesion01/`. Enseguida corremos la instrucción 

`$ python3.6 intro.py`