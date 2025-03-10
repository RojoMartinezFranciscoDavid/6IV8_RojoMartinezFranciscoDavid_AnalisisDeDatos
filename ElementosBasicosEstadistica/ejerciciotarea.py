import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

columnas_para_analizar= ['median_house_value', 'total_bedrooms', 'population']


def calcular_estadisticas(columnas):
    estadisticas = {
        'Media': np.mean(columnas),
        'Mediana': np.median(columnas),
        'Moda': columnas.mode().values,
        'Rango': np.ptp(columnas),
        'Varianza': np.var(columnas, ddof=1),
        'Desviación estándar': np.std(columnas, ddof=1)
    }
    return estadisticas


estadistica = {col: calcular_estadisticas(df[col].dropna()) for col in columnas_para_analizar}


for columna, stats in estadistica.items():
    print(f"\nEstadísticas de {columna}:")
    for key, value in stats.items():
        print(f"{key}: {value}")


def tabla_frecuencias(columnas):
    frecuencia = columnas.value_counts().sort_index()
    frecuencia_relativa = frecuencia / len(columnas)
    frecuencia_acumulada = frecuencia_relativa.cumsum()
    tabla_frecuencia = pd.DataFrame({
        'Valor': frecuencia.index,
        'Frecuencia': frecuencia.values,
        'Frecuencia Relativa': frecuencia_relativa.values,
        'Frecuencia Acumulada': frecuencia_acumulada.values
    })
    return tabla_frecuencia

# Mostrar tabla de frecuencias para 'median_house_value'
tabla_frecuencia = tabla_frecuencias(df['median_house_value'])
print("\nTabla de Frecuencia de median_house_value:")
print(tabla_frecuencia.head(10))  # Mostrar solo los primeros 10 valores

# Graficar histogramas
plt.figure(figsize=(12, 6))
sns.histplot(df['median_house_value'], bins=30, kde=True, color='blue', label='Media del Valor de la casa')
sns.histplot(df['total_bedrooms'], bins=30, kde=True, color='red', label='Total de Cuartos', alpha=0.6)
sns.histplot(df['population'], bins=30, kde=True, color='green', label='Suma', alpha=0.6)
plt.legend()
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma Comparativo')
plt.show()
