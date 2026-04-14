# Protocolo de Adaptación Viral en Modelo Murino (Ratón)

Este documento describe el procedimiento experimental para forzar la adaptación del SARS-CoV-2 en ratones de laboratorio, lo cual permite estudiar la evolución de variantes en tiempo real.

# Especificaciones del Modelo
- **Especie:** Mus musculus (Cepa BALB/c o C57BL/6).
- **Modificación:** Ratones transigénicos que expresan el receptor humano hACE2.

# Procedimiento de Pases Consecutivos
1. **Inóculo Inicial:** Se infecta al primer ratón (P0) con la cepa original (Wuhan-Hu-1).
2. **Recolección:** Tras 3 días post-infección, se recolecta tejido pulmonar y se homogeniza.
3. **Pase Serial:** El virus extraído del pulmón del ratón anterior se utiliza para infectar al siguiente ratón.
4. **Repetición:** Este proceso se repite durante **10 ciclos** (Pases).

# Análisis de Datos
Al finalizar los 10 pases, se realiza la extracción de ARN y secuenciación para comparar los resultados con la secuencia de referencia (NC_045512.2). El código para esta comparación se encuentra en la carpeta `/src`.
