# Sesión 1

## Actividades programadas:

* Introducción a Python.
* Programación de números naturales.
* Programación de sucesión de Fibonacci y número de Perrín.
* Recursión.

---

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