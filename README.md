# Instrucciones

## Instrucción general

1. Clone el repositorio de la prueba en su computador.
2. Crea una rama local con **su nombre** (i.e. jimena) sobre la que trabajará la prueba.
3. Resuelva los *dos* enunciados
4. Suba la rama al repositorio remoto con las respuestas

Consultas pueden contactar al correo electrónico: marco.espinozamarin@un.org

## Función de limpieza de datos
Se tienen datos de tres pasantes que ingresarán en el mes de agosto a la organización. No obstante, los datos necesitan limpiarse dado que estos vienen valores perdidos y caracteres especiales, por lo que se creó una función con el fin de que la limpieza de datos se realice de forma rápida y eficaz. Se le da una función de Python cuyo objetivo es limpiar un data frame de `pandas`. La función debe cumplir con las siguientes funcionalidades: 

1. Remover espacios vacios en columnas de tipo `string`.
2. Remover caracteres especiales (no alfanuméricos) de los campos.
3. Eliminar valores perdidos y reemplazarlos con strings vacios.

La función se encuentra en el archivo `test.py` y los datos en el archivo `data.csv`. Las instrucciones son:

1. Trabaje sobre el archivo `test.py`, donde primero cargue los datos y pruebe la función. Posteriormente: 
    - Identifique y explique de forma breve los errores de la función.
    - Dar una código corregido funcional con la implementación de las correcciones y explicar que cambios se implementaron.
    - Exporte el resultado en un archivo de excel con el siguiente formato: respuestas/**sunombre_test1.xlsx**
El resultado final esperado debe ser este:

| Nombre | Edad |
|--------|------|
| Marco  | 26   |
| Daniel |      |
| Maria  | 23   |

## Función de web-scrapping

En el archivo `test2.py` encontrará una función de web-scrapping con una aplicación. En la carpeta de *respuestas* crea un archivo *markdown* con las respuestas y llámelo: `test2_resp.md`. En base al código responda lo siguiente:

1. Explique de forma breve la lógica de la función. 
2. De forma breve responda en que casos es útil hacer web scraping secuencial y concurrente.
 