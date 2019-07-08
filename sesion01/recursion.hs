-- Definición de números naturales
data Nat = Z | S Nat deriving (Show,Eq)


-- Suma de números naturales
sumNat :: Nat -> Nat -> Nat
sumNat Z m = m
sumNat (S n) m = S (sumNat n m)
-- Ejemplo de ejecución
-- sumNat (S Z) (S $S Z)



--------------------------------------
-- Multiplicación de números naturales
multNat :: Nat -> Nat -> Nat
multNat Z _ = Z
multNat (S n) m = sumNat m (multNat n m)
-- Ejemplo de ejecución
-- multNat (S $S Z) (S $S $S $S Z)



--------------------------------------
-- Factorial
fact :: Int -> Int
fact n
  | n <= 0 = 1
  | otherwise = fact(n-1) * n
-- Ejemplo de ejecución
-- fact 58
-- fact 58786



--------------------------------------
-- Fibonacci
fib :: Int -> Int
fib n 
  | n<1 = error "El número de Fibonacci para un numero negativo esta indeterminado."
fib 1 = 1
fib 2 = 1
fib n = fib(n-1) + fib(n-2)
