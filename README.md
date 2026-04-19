# SARS-COVID-2-Comparador-Variantes

## Objetivo
Proyecto para comparar secuencias de variantes de SARS-COVID-2 obtenidas de pases consecutivos en un modelo de ratón para generar una variante "Mouse-adapted" que replique el ciclo infeccioso de humano y poder testear terapias/vacunas. En este repositorio desarollaremos el codigo para hacer las comparaciones de las variantes. 

## Secuencias
La sequencias obtenidas de cada pase se compararan con la secuencia parental y con la secuencia del pase anterior para obtener los cambios puntuales de cada variante. Las sequencias a analizar seran en este caso obtenidas a partir de datos de transcripcion de RNA viral en muestras de homogeneizado pulmonar. 

## Estructura del Repositorio
Para facilitar la navegación y la reproducibilidad del análisis, el proyecto se organiza de la siguiente manera:

* Datos : Almacenamiento de información genómica.
    * Datos crudos: Contiene la secuencia original de SARS-CoV-2 y archivos .fasta.
    * Datos procesados: Archivos curados y anotaciones (ej. archivos .gb).
* codigo : Carpeta con los scripts de procesamiento.
    * alignment.py: Script en Python diseñado para detectar cambios puntuales entre secuencias.
* docs : Documentación técnica y experimental.
    * protocolo_modelo_murino.md: Descripción del procedimiento de pases seriales en el modelo animal.
    * protocolo_SC2_MinION_sequencing.md: Descripcion de protocolo de amplificacion y secuenciacion "ARTIC SARS-CoV-2 sequencing protocol v4 (LSK114) V.4" de las muestras obtenidas en los pases.  
* resultados : Salidas detalladas del análisis.
    * Incluye reportes de mutaciones, figuras MA (.jpg) y conclusiones finales.

## Instalacion
Para usar este analizador hay que instalar la libreria Biopython

## Uso del codigo
Para realizar la comparacion de las variantes, se debe indicar tanto la ruta de la secuencia de la cepa parental como la de la secuencia del pase 

## Autores
Melany Pineda Garcia (Estudiante de Master de Bioinformatica)
Carmen de la Nuez Ramirez (Estudiante de Master de Bioinformatica)


