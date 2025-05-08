import numpy as np
import pandas as pd
from scipy.spatial import distance

puntos = {
    'Punto A': [2, 3],
    'Punto B': [5, 4],
    'Punto C': [1, 1],
    'Punto D': [6, 7],
    'Punto E': [3, 5],
    'Punto F': [8, 2],
    'Punto G': [4, 6],
    'Punto H': [2, 1]
}

df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print("Coordenadas de los puntos:")
print(df_puntos)

distancias_eu = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_mh = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_ch = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

for i in df_puntos.index:
    for j in df_puntos.index:
        # Distancia Euclidiana
        distancias_eu.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
        # Distancia Manhattan
        distancias_mh.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
        # Distancia Chebyshev
        distancias_ch.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

print("\nDistancias Euclidianas entre los puntos:")
print(distancias_eu)
print("\nDistancias Manhattan entre los puntos:")
print(distancias_mh)
print("\nDistancias Chebyshev entre los puntos:")
print(distancias_ch)

def encontrar_extremos(matriz_distancia):
    matriz_temp = matriz_distancia.copy()
    
    np.fill_diagonal(matriz_temp.values, np.nan)
    
    min_dist = np.nanmin(matriz_temp.values)
    min_idx = np.where(matriz_temp.values == min_dist)
    punto1_min, punto2_min = matriz_temp.index[min_idx[0][0]], matriz_temp.columns[min_idx[1][0]]
    
    max_dist = np.nanmax(matriz_temp.values)
    max_idx = np.where(matriz_temp.values == max_dist)
    punto1_max, punto2_max = matriz_temp.index[max_idx[0][0]], matriz_temp.columns[max_idx[1][0]]
    
    return (punto1_min, punto2_min, min_dist), (punto1_max, punto2_max, max_dist)

print("\n=== RESULTADOS DEL ANÁLISIS ===")

min_par_eu, max_par_eu = encontrar_extremos(distancias_eu)
print("\nDistancia Euclidiana:")
print(f"Puntos más cercanos: {min_par_eu[0]} y {min_par_eu[1]} con distancia {min_par_eu[2]:.4f}")
print(f"Puntos más alejados: {max_par_eu[0]} y {max_par_eu[1]} con distancia {max_par_eu[2]:.4f}")

min_par_mh, max_par_mh = encontrar_extremos(distancias_mh)
print("\nDistancia Manhattan:")
print(f"Puntos más cercanos: {min_par_mh[0]} y {min_par_mh[1]} con distancia {min_par_mh[2]:.4f}")
print(f"Puntos más alejados: {max_par_mh[0]} y {max_par_mh[1]} con distancia {max_par_mh[2]:.4f}")

min_par_ch, max_par_ch = encontrar_extremos(distancias_ch)
print("\nDistancia Chebyshev:")
print(f"Puntos más cercanos: {min_par_ch[0]} y {min_par_ch[1]} con distancia {min_par_ch[2]:.4f}")
print(f"Puntos más alejados: {max_par_ch[0]} y {max_par_ch[1]} con distancia {max_par_ch[2]:.4f}")