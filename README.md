# Instrucciones

## Función de limpieza de datos
Se tienen datos de tres pasantes que ingresarán en el mes de agosto a la organización. No obstante, los datos necesitan limpiarse dado que estos vienen valores perdidos y caracteres especiales, por lo que se creó una función con el fin de que la limpieza de datos se realice de forma rápida y eficaz. Se le da una función de Python cuyo objetivo es limpiar un data frame de `pandas`. La función debe cumplir con las siguientes funcionalidades: 

1. Remover espacios vacios en columnas de tipo `string`.
2. Remover caracteres especiales (no alfanuméricos) de los campos.
3. Eliminar valores perdidos y reemplazarlos con strings vacios.

La función se encuentra en el archivo `test.py` y los datos en el archivo `data.csv`. Las instrucciones son:

1. Trabaje sobre el archivo `test.py`, donde primero cargue los datos y pruebe la función. Posteriormente: 
    1.1 Identifique y explique de forma breve los errores de la función.
    1.2 Dar una código corregido funcional con la implementación de las correcciones y explicar que cambios se implementaron.
    1.3 Exporte el resultado en un archivo de excel con el siguiente formato: respuestas/**sunombre_test1.xlsx**
El resultado final esperado debe ser este:

| Nombre | Edad |
|--------|------|
| Marco  | 26   |
| Daniel |      |
| Maria  | 23   |