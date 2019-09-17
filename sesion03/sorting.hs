qSort :: [Int] -> [Int]
qSort [] = []
qSort (x:xs) = qSort [y | y<-xs,y<=x] ++ [x] ++ qSort[z | z<-xs, z>x]
