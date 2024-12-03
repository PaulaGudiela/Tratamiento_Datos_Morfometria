# Tratamiento_Datos_Morfometria
Este código busca tratar los datos de medidas morfométricas elaborados en tablas de excel, los cuales adicionalmente tengan invertido el orden del archivo, es decir, los nombres de las muestras o individuos en la primera fila y los nombres de las medidas en la primera columna.
Los archivos a tratar son del tipo .xlsx 
Mediante la manipulación de los datos de la siguiente forma: 
1. Transponer las filas y columnas dejando así los nombres de los individuos en la primera columna y los nombres de las medidas en la primera fila del archivo
2. Renombra la primera columna del archivo original, que luego será la primera fila del archivo transpuesto con el nombre de : muestras, con el fin de que en las manipulaciones siguientes no se elimine.
3. Eliminar los datos no númericos o inexistentes en el archivo
4. Dividir cada medida por la longitud estándar del respectivo individuo
5. Multiplicar todo esto por 100 con el fin de obtener los datos en % de Longitud estándar
6. Obtener el logaritmo natural de cada medida con el fin de estandarizar
7. Arrojar un documento en excel con esta manipulación de datos.
Es importante mencionar que se realizaron puntos de chequeo del código en cada manipulación de datos, por lo tanto, el código generará 8 documentos excel. Los primeros 7 de chequeo de cada punto individualmente y el último que será nombrado con el nombre del archivo orginal + datos_tratados 


El archivo de prueba es el: prueba_datos.xlsx 

El archivo erróneo que generará ciertos errores en el código y con el cual se le hicieron correcciones iniciales es: error_datos.xlsx
