import numpy as np
import matplotlib.pyplot as plt

#vamos a crear una semilla random para repruductibilidad
np.random.seed(0)

#vamos a buscar los parametros para una distribución
#media
media = 0
#desviación estándar
sigma1= 1
sigma2 = 2
sigma3 = 3

#el número mde muestras para el análisis 
n_muestras = 1000

#vamos a generar los datos de las distribuciones normales
data1= np.random.normal(media, sigma1, n_muestras)
data3= np.random.normal(media, sigma2, n_muestras)
data2= np.random.normal(media, sigma3, n_muestras)

#vamos a configurar la gráfica
plt.figure(figsize=(10,6))

#vamos a cargar las frecuencias a partir de una gráfica de histograma
plt.hist(data1, bins=30, color='purple', density=True, label='Desviación estándar 1', alpha =0.5)

plt.hist(data2, bins=30, color='pink', density=True, label='Desviación estándar 2', alpha =0.5)

plt.hist(data3, bins=30, color='red', density=True, label='Desviación estándar 3', alpha =0.5)

# a graficar

plt.title('Comparación de distribuciones Normales en random')
plt.xlabel('Value')
plt.ylabel('Density')
plt.axhline(0, color= 'black', linewidth=0.5, ls='--') 
plt.axhline(0, color= 'black', linewidth=0.5, ls='--') 
plt.legend()
plt.grid()

plt.show()