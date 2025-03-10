import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo housing.csv
df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

# Seleccionar las columnas necesarias
columns_to_analyze = ['median_house_value', 'total_bedrooms', 'population']

# Función para calcular estadísticas
def calculate_statistics(column):
    stats = {
        'Media': np.mean(column),
        'Mediana': np.median(column),
        'Moda': column.mode().values,
        'Rango': np.ptp(column),
        'Varianza': np.var(column, ddof=1),
        'Desviación estándar': np.std(column, ddof=1)
    }
    return stats

