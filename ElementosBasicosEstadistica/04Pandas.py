import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#mostrar las primeras 5 filas
print(df.head())

#mostrar las ultimas 5
print (df.tail())

#mostrar una fila especifica
print(df.iloc[7])

#mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#mostrar la media de total_rooms
mediadecuarto = df ["total_rooms"]. mean()
print('La media total es: ' , mediadecuarto)

#mediana
medianadecuarto = df['median_house_value'].median()
print('La mediana total es: ' , medianadecuarto)

#la suma de popular
salariototal = df['population'].sum()
print('El salario total es de : ', salariototal)

#poder filtrar

vamoshacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamoshacerunfiltro)


#un grafico de dispersion
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])

#nombrar ejes
plt.xlabel("proximidad")
plt.ylabel("Precio")

plt.title("Gráfico de Dispersión de Proximidad al oceano vs Precio")
plt.show()