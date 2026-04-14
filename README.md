# SARS-COVID-2-Comparador-Variantes
Proyecto para comparar secuencias de variantes de SARS COVID2 obtenidas de pases consecutivos en un modelo de ratón para generar una variante "Mouse-adapted" que replique el ciclo infeccioso de humano y poder testear terapias/vacunas.

## Secuencias
La sequencias obtenidas de cada pase se compararan con la secuencia parental y con la secuencia del pase anterior para obtener los cambios puntuales de cada variante. Las sequencias a analizar seran en este caso obtenidas a partir de datos de transcripcion de RNA. 

## Estructura del Repositorio
Para facilitar la navegación y la reproducibilidad del análisis, el proyecto se organiza de la siguiente manera:

* **Datos/**: Almacenamiento de información genómica.
    * `Datos crudos/`: Contiene la secuencia original de SARS-CoV-2 y archivos `.fasta`.
    * `Datos procesados/`: Archivos curados y anotaciones (ej. archivos `.gb`).
* **codigo/**: Carpeta con los scripts de procesamiento.
    * `alignment.py`: Script en Python diseñado para detectar cambios puntuales entre secuencias.
* **docs/**: Documentación técnica y experimental.
    * `protocolo_modelo_murino.md`: Descripción del procedimiento de pases seriales en el modelo animal.
* **resultados/**: Salidas detalladas del análisis.
    * Incluye reportes de mutaciones, figuras MA (`.jpg`) y conclusiones finales.


