import pandas as pd

#lo ocupé para unir los exceles :p
uno = pd.read_excel("ElementosBasicosEstadistica/proyecto1.xlsx")
dos = pd.read_excel("ElementosBasicosEstadistica/Catalogo_sucursal.xlsx")
uno_combinado = pd.concat([uno,dos])
uno_combinado.to_excel("unoydos.xlsx", index= False)

#puntito 1 <3
def Ventastotales  (unoydos.xlsx):
    try:
        df_ventas = pd.read_excel(unoydos.xlsx)

        ventas_totales = 'ventas_tot'  
        
        if ventas_totales in df_ventas.columns:
            ventas_totales = df_ventas[ventas_totales].sum()
            
            print(f"\nVentas totales: ${ventas_totales:.2f}")
            
            return ventas_totales, df_ventas
        else:
            print(f"Error: No se encuentra la columna '{ventas_totales}' en el archivo.")
            return None, df_ventas
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {unoydos.xlsx}")
        return None, None
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")
        return None, None

ruta_archivo = 'ElementosBasicosEstadistica/unoydos.xlsx'
total_ventas, df_ventas = Ventastotales('ventas_tot')


