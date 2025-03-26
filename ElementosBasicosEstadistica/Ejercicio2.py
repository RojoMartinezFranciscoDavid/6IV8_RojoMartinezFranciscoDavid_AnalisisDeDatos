import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

uno = pd.read_excel("ElementosBasicosEstadistica/proyecto1.xlsx")
dos = pd.read_excel("ElementosBasicosEstadistica/Catalogo_sucursal.xlsx")
uno_combinado = pd.concat([uno,dos])
uno_combinado.to_excel("unoydos.xlsx", index= False)

RUTA_EXCEL = r'C:\Users\Maricela\Desktop\6IV8_RojoMartinezFranciscoDavid_AnalisisDeDatos\6IV8_RojoMartinezFranciscoDavid_AnalisisDeDatos\unoydos.xlsx'
CARPETA_SALIDA = r'C:\Users\Maricela\Desktop\6IV8_RojoMartinezFranciscoDavid_AnalisisDeDatos\6IV8_RojoMartinezFranciscoDavid_AnalisisDeDatos\Analisis_Ventas'

def cargar_datos(ruta_archivo):
    try:
        df = pd.read_excel(ruta_archivo, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def calcular_ventas_totales(df):
    ventas_totales = df['ventas_tot'].sum()
    return ventas_totales

def analisis_adeudos(df):
    total_clientes = df['no_clientes'].sum()
    clientes_con_adeudo = df[df['B_adeudo'] > 0]['no_clientes'].sum()
    clientes_sin_adeudo = total_clientes - clientes_con_adeudo
    
    porcentaje_con_adeudo = (clientes_con_adeudo / total_clientes) * 100
    porcentaje_sin_adeudo = (clientes_sin_adeudo / total_clientes) * 100
    
    return {
        'total_clientes': total_clientes,
        'clientes_con_adeudo': clientes_con_adeudo,
        'clientes_sin_adeudo': clientes_sin_adeudo,
        'porcentaje_con_adeudo': porcentaje_con_adeudo,
        'porcentaje_sin_adeudo': porcentaje_sin_adeudo
    }

def grafica_ventas_tiempo(df):
    plt.figure(figsize=(12, 6))
    ventas_por_mes = df.groupby('B_mes')['ventas_tot'].sum()
    ventas_por_mes.plot(kind='bar')
    plt.title('Ventas Totales por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Ventas Totales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CARPETA_SALIDA + '\\ventas_por_mes.png')
    plt.close()

def grafica_desviacion_pagos(df):
    plt.figure(figsize=(12, 6))
    desviacion_pagos = df.groupby('B_mes')['pagos_tot'].std()
    desviacion_pagos.plot(kind='bar')
    plt.title('Desviación Estándar de Pagos por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Desviación Estándar de Pagos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CARPETA_SALIDA + '\\desviacion_pagos.png')
    plt.close()

def calcular_deuda_total(df):
    deuda_total = df['adeudo_actual'].sum()
    return deuda_total

def calcular_porcentaje_utilidad(df):
    ventas_totales = df['ventas_tot'].sum()
    deuda_total = df['adeudo_actual'].sum()
    porcentaje_utilidad = ((ventas_totales - deuda_total) / ventas_totales) * 100
    return porcentaje_utilidad

def grafica_ventas_sucursal(df):
    ventas_por_sucursal = df.groupby('id_sucursal')['ventas_tot'].sum()
    plt.figure(figsize=(10, 10))
    plt.pie(ventas_por_sucursal, labels=ventas_por_sucursal.index, autopct='%1.1f%%')
    plt.title('Ventas por Sucursal')
    plt.axis('equal')
    plt.savefig(CARPETA_SALIDA + '\\ventas_sucursal.png')
    plt.close()

def grafica_deudas_utilidad_sucursal(df):
    datos_sucursal = df.groupby('id_sucursal').agg({
        'adeudo_actual': 'sum',
        'ventas_tot': 'sum'
    }).reset_index()
    
    datos_sucursal['margen_utilidad'] = (datos_sucursal['ventas_tot'] - datos_sucursal['adeudo_actual']) / datos_sucursal['ventas_tot'] * 100
    
    plt.figure(figsize=(12, 6))
    
    x = np.arange(len(datos_sucursal['id_sucursal']))
    width = 0.35
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.bar(x - width/2, datos_sucursal['adeudo_actual'], width, label='Deuda Total', color='red', alpha=0.7)
    ax1.set_ylabel('Deuda Total')
    ax1.set_xlabel('ID Sucursal')
    
    ax2 = ax1.twinx()
    ax2.bar(x + width/2, datos_sucursal['margen_utilidad'], width, label='Margen Utilidad (%)', color='green', alpha=0.7)
    ax2.set_ylabel('Margen de Utilidad (%)')
    
    plt.title('Deudas y Margen de Utilidad por Sucursal')
    ax1.set_xticks(x)
    ax1.set_xticklabels(datos_sucursal['id_sucursal'])
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig(CARPETA_SALIDA + '\\deudas_utilidad_sucursal.png')
    plt.close()

def main():
    df = cargar_datos(RUTA_EXCEL)
    
    if df is not None:
        ventas_totales = calcular_ventas_totales(df)
        print(f"Ventas Totales: ${ventas_totales:,.2f}")
        
        analisis_adeudo = analisis_adeudos(df)
        print("\nAnálisis de Adeudos:")
        print(f"Total Clientes: {analisis_adeudo['total_clientes']}")
        print(f"Clientes con Adeudo: {analisis_adeudo['clientes_con_adeudo']} ({analisis_adeudo['porcentaje_con_adeudo']:.2f}%)")
        print(f"Clientes sin Adeudo: {analisis_adeudo['clientes_sin_adeudo']} ({analisis_adeudo['porcentaje_sin_adeudo']:.2f}%)")
        
        grafica_ventas_tiempo(df)
        grafica_desviacion_pagos(df)
        
        deuda_total = calcular_deuda_total(df)
        print(f"\nDeuda Total: ${deuda_total:,.2f}")
        
        porcentaje_utilidad = calcular_porcentaje_utilidad(df)
        print(f"Porcentaje de Utilidad: {porcentaje_utilidad:.2f}%")
        
        grafica_ventas_sucursal(df)
        grafica_deudas_utilidad_sucursal(df)
        
        print("\nTodas las gráficas han sido generadas y guardadas.")

if __name__ == "__main__":
    main()