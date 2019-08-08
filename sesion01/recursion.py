## -----------------------------------------------------
## Factorial
def fact(n):
    if n <= 0:
        return 1
    else:
        return n*fact(n-1)

## Execution
n_fact = 99
print('Resultado de la llamada a la funcion fact(',n_fact,'):')
print(fact(n_fact),'\n')


## -----------------------------------------------------
## Fibonacci
def fib(i):
    if i<0:
        return 'El número de Fibonacci para un numero entero negativo esta indeterminado.'
    elif i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)

## Execution
n_fib = 100
print('El número de Fibonacci en la posición',n_fib,' es ',fib(n_fib),'\n')

#print('La serie de Fibonacci de 0 al',n_fib,':')
#print([fib(k) for k in range(n_fib + 1)],'\n')


## -----------------------------------------------------
## Perrin
def perrin(i):
    if i<0:
        return 'El número de Perrin para un numero entero negativo esta indeterminado.'
    elif i == 0:
        return 3
    elif i == 1:
        return 0
    elif i == 2:
        return 2
    else:
        return perrin(i-2) + perrin(i-3)

def perrin_list(n):
    if n < 0:
        return []
    elif n == 0:
        return [perrin(0)]
    else:
        return perrin_list(n-1) + [perrin(n)]

## Execution
n_perrin = 30
print('La serie de Perrin de 0 al',n_perrin,':')
print(perrin_list(n_perrin))
