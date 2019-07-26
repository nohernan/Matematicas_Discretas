import numpy as np 
import matplotlib.pyplot as plt 

# Arreglo de entrada a las funciones
# logatirmo: 1000 números tomandos de manera
# uniforme entre 0.001 y 11
in_array = np.linspace(0.001,11,1000)

plt.figure()

# Establecemos el rango del eje x
plt.xlim((-1,11))
# Establecemos el rango del eje y
plt.ylim((-6,11))

# Función identidad
plt.plot(range(-1,11), range(-1,11),  
         color = 'dimgray',label='f(x)=x',ls=':')

# Logaritmo base 1.5
plt.plot(in_array, np.log(in_array)/np.log(1.5),
         color = 'brown', label='log1.5')

# Logaritmo base 2
plt.plot(in_array, np.log2(in_array),  
         color = 'green',label='log2')

# Logaritmo natural
plt.plot(in_array, np.log(in_array),  
         color = 'blue',label='ln')

# Logaritmo base 10
plt.plot(in_array, np.log10(in_array),  
         color = 'red', label='log10')
  
# Dibujamos y etiquetamos el eje x
plt.axhline(0, color='black')
plt.text(10.5,-0.5,'x')
# Dibujamos y etiquetamos el eje y
plt.axvline(0, color='black')
plt.text(0.25,10.5,'y')

# La etiquetas las ponemos arriba al centro
plt.legend(loc='upper center')

# Establecemos el título de la gráfica
plt.title("Logaritmos")

# Mostramos la gráfica
plt.show()  
