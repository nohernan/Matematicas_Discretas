-- Definición de números naturales
data Nat = Z | S Nat deriving (Show,Eq)


--------------------------------------
-- Suma de números naturales
sumNat :: Nat -> Nat -> Nat
sumNat Z m = m
sumNat (S n) m = S (sumNat n m)


--------------------------------------
-- Multiplicación de números naturales
multNat :: Nat -> Nat -> Nat
multNat Z _ = Z
multNat (S n) m = sumNat m (multNat n m)


--------------------------------------
-- Factorial
fact :: Int -> Int
fact n
  | n <= 0 = 1
  | otherwise = fact(n-1) * n


--------------------------------------
-- Fibonacci
fib :: Int -> Int
fib n 
  | n<1 = error "El número de Fibonacci para un numero negativo esta indeterminado."
fib 1 = 1
fib 2 = 1
fib n = fib(n-1) + fib(n-2)
