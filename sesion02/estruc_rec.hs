-- Definición de fórmulas de la lógica proposicional
data FormProp = V | Atom String | No FormProp | Disy FormProp FormProp | Conj FormProp FormProp | Imp FormProp FormProp deriving Show

