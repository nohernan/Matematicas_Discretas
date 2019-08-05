-- Función que calcula duplica su argumento
doble x = x + x


-- Función que toma dos números, los duplica y entonces los suma
doble_suma:: Int -> Int -> Int
doble_suma x y = doble x + doble y


-- Función que duplica aquellos números que son mayores o iguales que 100 y menores que 150. En otro caso, la función divide entre 2 al argumento
doble_condicion z =
   if z >= 100 && z < 150
     then z*2
     else z/2


-- Uso de 'let' para calcular (x+1)+(x+1)^2+(x+1)^3
polinomio x = let suma = x + 1 
              in suma+suma^2+suma^3


-- Ejemplo del uso de 'where'. Dada una lista se intercambian el primero
-- y el último símbolo. Así, inter_pos [1,2,3,4] = [4,2,3,1]
-- También se ejemplifica el uso del operador de asociación '$'
inter_pos lst = if lst == []
                then []
                else ult:res
  where
    rev  = reverse lst
    ult  = head rev
    lst2 = reverse $ tail rev
    res  = if lst2 == [] then [] else (tail lst2) ++ [head lst2]


-- Composición de funciones

-- Funciones anónimas

-- Listas por comprensión

intSqrt = floor . sqrt . fromInteger

es_primo n = not $ any (\x -> n `mod` x == 0) [2..intSqrt n]

primeros_primos y = [ x | x<-[2..y], es_primo x]