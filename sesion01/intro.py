##
## Definition adjacentElementsProduct
def adjacentElementsProduct(inputArray):

   val = inputArray[0]*inputArray[1]
   
   if len(inputArray) <= 2 :
      return val
         
   for i in range(len(inputArray) - 2):
      v1 = inputArray[i+1]
      v2 = inputArray[i+2]
      val = max([val, v1*v2])
      
   return val

## Execution
adj_array = [9, 5, 10, 2, 24, -1, -48]
print('Resultado de la llamada a la funcion adjacentElementsProduct(',adj_array,'):')
print(adjacentElementsProduct(adj_array),'\n')


## -----------------------------------------------------
## Definition of function allLongestStrings
def allLongestStrings(inputArray):

   max_size = 0
   final_arr = []
   
   for st in inputArray:
      st_size = len(st)
      if (st_size>max_size):
         max_size = st_size
         final_arr = [st]
      elif (len(st)==max_size):
         final_arr.append(st)
    
   return final_arr

## Execution
all_array = ["young","yooooooung","hot","or","not","come","on","fire","water","watermelon"]
print('Resultado de la llamada a la funcion allLongestStrings(',all_array,'):')
print(allLongestStrings(all_array),'\n')


## -----------------------------------------------------
## Definition of function alternatingSums
def alternatingSums(a):
   return [sum(a[0::2]),sum(a[1::2])]

## Execution
alternating_array = [10,1,55,59,101,205,35]
print('Resultado de la llamada a la funcion alternatingSums(',alternating_array,'):')
print(alternatingSums(alternating_array),'\n')


## -----------------------------------------------------
## Definition of function alternatingSums_rec (recursive version)
def alternatingSums_rec(a):
    if (len(a) == 0):
        return [0, 0]
    elif (len(a) == 1):
        return [a[0], 0]
    else:
        v1 = a[0] + (alternatingSums_rec(a[2:]))[0]
        v2 = a[1] + (alternatingSums_rec(a[2:]))[1]
        return [v1, v2]
        
## Execution
alternating_array_rec = [10,1,55,59,101,205,35]
print('Resultado de la llamada a la funcion alternatingSums_rec(',alternating_array_rec,'):')
print(alternatingSums_rec(alternating_array_rec))
