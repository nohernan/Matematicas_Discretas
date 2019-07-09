##
## Definition adjacentElementsProduct
def adjacentElementsProduct(inputArray):

   val = inputArray[0]*inputArray[1]
   
   if len(inputArray) <= 2 :
      print(val)

      return
         
   for i in range(len(inputArray) - 2):
      v1 = inputArray[i+1]
      v2 = inputArray[i+2]
      val = max([val, v1*v2])
      
   print(val)

## Execution
adj_array = [9, 5, 10, 2, 24, -1, -48]
print("Resultado de la llamda a la funcion adjacentElementsProduct("+str(adj_array)+"):")
adjacentElementsProduct(adj_array)
print("")

##
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
    
   print(final_arr)

## Execution
all_array = ["young","yooooooung","hot","or","not","come","on","fire","water","watermelon"]
print("Resultado de la llamada a la funcion allLongestStrings("+str(all_array)+"):")
allLongestStrings(all_array)
