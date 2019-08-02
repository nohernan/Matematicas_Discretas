-- Definición de valores booleanos
data ValBool = V | F deriving (Show,Eq)


-- Definición de fórmulas de la lógica proposicional
data FormProp = Const ValBool | Atom Char | No FormProp | Disy FormProp FormProp | Conj FormProp FormProp | Imp FormProp FormProp deriving Show


-- Función de interpretación para fórmulas de la lógica proposicional
inter :: (Char -> ValBool) -> FormProp -> ValBool
inter _ (Const V) = V
inter asig (Atom p) = asig p
inter asig (No phi)
  | (inter asig phi) == V = F
  | otherwise = V
inter asig (Disy phi psi) 
  | (inter asig phi) == F && (inter asig psi) == F = F
  | otherwise = V
inter asig (Conj phi psi)
  | (inter asig phi) == V && (inter asig psi) == V = V
  | otherwise = F
inter asig (Imp phi psi)
  | (inter asig phi) == V && (inter asig psi) == F = F
  | otherwise = V


-- Asignación particular de variables proposicionales
mi_asig :: Char -> ValBool
mi_asig c
  | c == 'p' = V
  | c == 'q' = V
  | otherwise = error "Variable proposicional sin definir"



--------------------------------------------------------
--------------------------------------------------------
-- Definición de listas
data Lista a = Nil | Cons a (Lista a) deriving Show


-- Concatenación de listas
concatenacion :: Lista a -> Lista a -> Lista a
concatenacion Nil l = l
concatenacion (Cons x l1) l2 = Cons x (concatenacion l1 l2)



--------------------------------------------------------
--------------------------------------------------------
-- Definición de árboles binarios
data Tree a = Vacio | Nodo a (Tree a) (Tree a) deriving (Show,Eq)


-- Función que determina si un árbol es subárbol de otro
subarbol _ Vacio = True
subarbol Vacio _ = False
subarbol (Nodo a t1 t2) (Nodo b k1 k2)
  | a == b && t1 == k1 && t2 == k2 = True
  | subarbol t1 (Nodo b k1 k2) || subarbol t2 (Nodo b k1 k2) = True
  | otherwise = False

