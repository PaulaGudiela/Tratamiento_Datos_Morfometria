import pandas as pd
import numpy as np

# Ruta del archivo de entrada, aqui se debe poner el nombre del archivo a leer
archivo_entrada = 'prueba_datos.xlsx'

# Leer el archivo Excel
df = pd.read_excel(archivo_entrada) #En esta linea se carga el archivo excel en un dataframe (df)

# Guardar el archivo original como punto de verificación en un excel
df.to_excel('01_archivo_original.xlsx', index=False)
print("Archivo original guardado como: 01_archivo_original.xlsx")

# Transponer el DataFrame para que las medidas estén en las columnas
df_transpuesto = df.set_index(df.columns[0]).T  #Usa la primera columna como índice y transpone filas por columnas
# Guardar después de la transposición
df_transpuesto.to_excel('02_archivo_transpuesto.xlsx', index=True)
print("Archivo después de la transposición guardado como: 02_archivo_transpuesto.xlsx")

# Renombrar la primera columna como 'Muestras' para que las muestras estén en el índice
df_transpuesto.rename(columns={df_transpuesto.columns[0]: 'Muestras'}, inplace=True)
# Guardar después de renombrar la primera columna
df_transpuesto.to_excel('03_archivo_renombrado.xlsx', index=True)
print("Archivo después de renombrar la primera columna guardado como: 03_archivo_renombrado.xlsx")

# Eliminar las filas que tienen datos no numéricos (excepto la columna 'Muestras')
# Convierto todos los valores a numéricos y elimino las filas con valores no válidos
df_transpuesto = df_transpuesto[df_transpuesto.drop(columns='Muestras', errors='ignore').apply(
    lambda x: pd.to_numeric(x, errors='coerce')).notnull().all(axis=1)]
# Guardar después de eliminar filas con datos no numéricos
df_transpuesto.to_excel('04_archivo_sin_filas_invalidas.xlsx', index=True)
print("Archivo después de eliminar filas con datos no numéricos guardado como: 04_archivo_sin_filas_invalidas.xlsx")

# Dividir cada valor de las filas por el valor de la columna B de cada fila
df_transpuesto.iloc[:, 0:] = df_transpuesto.iloc[:, 0:].apply(
    lambda row: row / row.iloc[0], axis=1)

# Guardar después de realizar la división
df_transpuesto.to_excel('05_archivo_dividido_por_columna_B.xlsx', index=True)
print("Archivo después de dividir por la columna B guardado como: 05_archivo_dividido_por_columna_B.xlsx")


# Multiplicar por 100 todo, excepto la primera fila, la primera columna y la segunda columna
df_transpuesto.iloc[0:, 1:] = df_transpuesto.iloc[0:, 1:] * 100

# Guardar después de multiplicar por 100
df_transpuesto.to_excel('06_archivo_multiplicado_por_100.xlsx', index=True)
print("Archivo después de multiplicar por 100 guardado como: 06_archivo_multiplicado_por_100.xlsx")

# Aplicar logaritmo natural a todas las celdas excepto la primera fila, primera columna y segunda columna
df_transpuesto.iloc[0:, 1:] = df_transpuesto.iloc[0:, 1:].apply(
    lambda row: row.apply(lambda x: np.log(x) if isinstance(x, (int, float)) and np.isfinite(x) else x)
, axis=1)

# Guardar después de aplicar el logaritmo natural
df_transpuesto.to_excel('07_archivo_logaritmo_aplicado.xlsx', index=True)
print("Archivo después de aplicar el logaritmo natural guardado como: 07_archivo_logaritmo_aplicado.xlsx")

#Guardar el archivo final, tomando el nombre del archivo original + datos tratados
nuevo_nombre = archivo_entrada.replace('.xlsx', '_datos_tratados.xlsx')
df_transpuesto.to_excel(nuevo_nombre, index=True)
print(f'Archivo procesado guardado como: {nuevo_nombre}')
