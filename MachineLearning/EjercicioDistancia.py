#Calcular distancias entre todos los pares de puntos y determinar cuáles están más alejados entre sí y cuáles están más cercanos utilizando las distancias: Euclideana, Manhattan y ChebyShev

import numpy as np
import pandas as pd
from scipy.spatial import distance

#Definimos las coordenadas de las puntos

puntos={
    'Tienda A':[2, 3],
    'Tienda B':[5, 4],
    'Tienda C':[1, 1],
    'Tienda D':[6, 7],
    'Tienda E':[3, 5],
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
    
    
}



df_puntos= pd.DataFrame(puntos).T
df_puntos.columns=['X','Y']
print("coordenadas de las puntos")
print(df_puntos)

def calcular_distancias(puntos):
    distancias=pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i!=j: #No calcula la distancia del mismo punto
                #Distancia Euclidiana
                distancias.loc[i,j]= distance.euclidean(df_puntos.loc[i],df_puntos.loc[j])
    return distancias
distancias= calcular_distancias(puntos)
valor_maximo=distancias.values.max()
(punto1,punto2)= distancias.stack().idxmax()
print('Tabla de Distancias')
print(distancias)
print('Distancia Máxima: ',valor_maximo)
print('Entre el punto: ',punto1,'; y el punto: ',punto2)


#Another way to calculate the distance
max_value=distancias.max().max()
#get the column that includes the maxium value
col_max=distancias.max().idxmax()

#get the index(fila) that includes the maxium value
id_max=distancias[col_max].idxmax()

print(f"Valor máximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Índice: {id_max}")