-- Función que duplica su argumento
doble x = x + x


-- Función que toma dos números, los duplica y entonces los suma
doble_suma:: Int -> Int -> Int
doble_suma x y = doble x + doble y


-- Función que duplica aquellos números que son mayores o iguales que 100 y menores que 150. En otro caso, la función divide entre 2 al argumento
doble_condicion z =
   if z >= 100 && z < 150
     then z*2
     else z/2


-- Composición de funciones
doble_doble = doble_condicion . doble


-- Uso de 'let' para calcular 1+(x+y)+(x+y)^2+(x+y)^3
polinomio x y = let suma = x + y 
                in 1+suma+suma^2+suma^3


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


-- Funciones anónimas
valor_abs_listas xs = filter (\x-> mod x 2 == 0) xs


-- Listas por comprensión
serie_geo :: Int -> Int -> [Int]
serie_geo r exp = [r^n | n<-[0..exp]]

serie_geo_valor :: Int -> Int -> Int
serie_geo_valor r exp = sum $ serie_geo r exp


-- Las función primeros_primos genera una lista de primos menores o iguales al
-- argumento de la función. Para ello se necesitan de las funciones intSqrt y es_primo
intSqrt = floor . sqrt . fromInteger

es_primo n = not $ any (\x -> n `mod` x == 0) [2..intSqrt n]

primeros_primos y = [ x | x<-[2..y], es_primo x]