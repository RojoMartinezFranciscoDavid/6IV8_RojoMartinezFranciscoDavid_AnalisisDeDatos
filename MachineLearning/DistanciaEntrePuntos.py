import numpy as np
import pandas as pd
from scipy.spatial import distance



tiendas={
    'Tienda A':[2, 3],
    'Tienda B':[5, 4],
    'Tienda C':[1, 1],
    'Tienda D':[6, 7],
    'Tienda E':[3, 5],
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
    
}


df_tiendas= pd.DataFrame(tiendas).T
df_tiendas.columns=['X','Y']
print("coordenadas de las tiendas")
print(df_tiendas)



distancias_eu=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_mh=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_ch=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)



for i in df_tiendas.index:
    for j in df_tiendas.index:
        #Distancia Euclidiana:
        distancias_eu.loc[i,j]=distance.euclidean(df_tiendas.loc[i],df_tiendas.loc[j])
        #Distancia Manhattan
        distancias_mh.loc[i,j]=distance.cityblock(df_tiendas.loc[i],df_tiendas.loc[j])
        #Distancia Cheby
        distancias_ch.loc[i,j]=distance.chebyshev(df_tiendas.loc[i],df_tiendas.loc[j])
        

print("\nDistancias Euclideanas entre las tiendas: ")
print(distancias_eu)
print("\nDistancias Manhattan entre las tiendas: ")
print(distancias_mh)
print("\nDistancias Chebyshev entre las tiendas: ")
print(distancias_ch)