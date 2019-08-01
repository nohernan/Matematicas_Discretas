data ValBool = V | F deriving (Show,Eq)

-- Definición de fórmulas de la lógica proposicional
data FormProp = Const ValBool | Atom Char | No FormProp | Disy FormProp FormProp | Conj FormProp FormProp | Imp FormProp FormProp deriving Show

mi_asig :: Char -> ValBool
mi_asig c
  | c == 'p' = V
  | c == 'q' = V
  | otherwise = F

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