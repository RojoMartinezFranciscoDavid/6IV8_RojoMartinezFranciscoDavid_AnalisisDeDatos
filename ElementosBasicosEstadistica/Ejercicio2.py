import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#ahí le pone usted su ruta :p
uno = pd.read_excel(r"C:\Users\adolf\OneDrive\OneDrive - Instituto Politecnico Nacional\Desktop\IAAd\6IV8_RojoMartinezFranciscoDavid_AnalisisDeDatos\ElementosBasicosEstadistica\proyecto1.xlsx")
dos = pd.read_excel(r"C:\Users\adolf\OneDrive\OneDrive - Instituto Politecnico Nacional\Desktop\IAAd\6IV8_RojoMartinezFranciscoDavid_AnalisisDeDatos\ElementosBasicosEstadistica\Catalogo_sucursal.xlsx")
uno_combinado = pd.concat([uno,dos])
uno_combinado.to_excel("unoydos.xlsx", index= False)

df = pd.read_excel(r"C:\Users\adolf\OneDrive\OneDrive - Instituto Politecnico Nacional\Desktop\IAAd\6IV8_RojoMartinezFranciscoDavid_AnalisisDeDatos\ElementosBasicosEstadistica\unoydos.xlsx")


ventas_tot = df["ventas_tot"].sum()
print('La suma de las ventas totales es:', ventas_tot)


tot_adeudo = df[df["adeudo_actual"] > 0].shape[0]
tot_no_adeudo = df[df["adeudo_actual"] == 0].shape[0]

porcen_adeudo = (tot_adeudo / len(df)) * 100
porcen_no_adeudo = (tot_no_adeudo / len(df)) * 100

print('La cantidad de socios con adeudos:', tot_adeudo, '(', round(porcen_adeudo, 2), '%)')
print('La cantidad de socios sin adeudos:', tot_no_adeudo, '(', round(porcen_no_adeudo, 2), '%)')


plt.figure(figsize=(10, 5))
plt.bar(df["B_mes"], df["ventas_tot"], color='blue')
plt.xlabel("Fecha")
plt.ylabel("Ventas Totales")
plt.title("Ventas Totales respecto al Tiempo")
plt.xticks(rotation=45)
plt.show()


std_pagos = df.groupby("B_mes")["pagos_tot"].std()
plt.figure(figsize=(10, 5))
plt.plot(std_pagos.index, std_pagos.values, marker='o', linestyle='-', color='red')
plt.xlabel("Fecha")
plt.ylabel("Desviación Estándar de Pagos")
plt.title("Desviación Estándar de Pagos respecto al Tiempo")
plt.xticks(rotation=45)
plt.show()


deuda_tot = df["adeudo_actual"].sum()
print('La deuda total de los clientes es:', deuda_tot)


utilidad = ventas_tot - deuda_tot
porcentaje_utilidad = (utilidad / ventas_tot) * 100 if ventas_tot > 0 else 0
print('El porcentaje de utilidad del comercio es:', round(porcentaje_utilidad, 2), '%')


ventas_sucursal = df.groupby("suc")["ventas_tot"].sum()
plt.figure(figsize=(8, 8))
plt.pie(ventas_sucursal, labels=ventas_sucursal.index, autopct='%1.1f%%', startangle=140)
plt.title("Ventas por Sucursal")
plt.show()


fig, ax = plt.subplots(figsize=(10, 5))
deudas_sucursal = df.groupby("suc")["adeudo_actual"].sum()
ax.bar(deudas_sucursal.index, deudas_sucursal.values, color='orange', label='Deuda Total')
plt.xticks(rotation=45)
plt.show()

ventas_por_sucursal = df.groupby("suc")["ventas_tot"].sum()
deudas_por_sucursal = df.groupby("suc")["adeudo_actual"].sum()
utilidad_por_sucursal = ventas_por_sucursal - deudas_por_sucursal
margen_utilidad_por_sucursal = (utilidad_por_sucursal / ventas_por_sucursal) * 100


fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(deudas_por_sucursal.index, deudas_por_sucursal.values, color='orange', label='Deuda Total')
ax1.set_xlabel('Sucursal')
ax1.set_ylabel('Deuda Total', color='orange')
ax1.tick_params(axis='y', labelcolor='orange')

ax2 = ax1.twinx()
ax2.plot(margen_utilidad_por_sucursal.index, margen_utilidad_por_sucursal.values, 'ro-', label='Margen de Utilidad (%)')
ax2.set_ylabel('Margen de Utilidad (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.title('Deudas Totales vs Margen de Utilidad por Sucursal')
plt.xticks(rotation=45)
plt.show()
