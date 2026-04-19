#Codigo de ejemplo para efectos de la tarea

def analizar_variantes(seq_referencia, seq_muestra):
    """
    Compara dos secuencias y devuelve una lista de mutaciones encontradas.
    """
    mutaciones = []
    
    # Usamos zip para comparar ambas secuencias posición por posición
    for i, (base_ref, base_mut) in enumerate(zip(seq_referencia, seq_muestra)):
        if base_ref != base_mut:
            posicion = i + 1  # +1 porque en biología no empezamos a contar en 0
            mutaciones.append({
                "posicion": posicion,
                "de": base_ref,
                "a": base_mut
            })
    
    return mutaciones

# --- SIMULACIÓN DE DATOS ---
# Secuencia original (Wuhan-Hu-1 fragmento)
secuencia_wuhan = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCT"

# Secuencia tras 10 pases en ratón (con 2 mutaciones inventadas)
secuencia_pase10 = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGGTCTCTTGTAGATGT"
#                                                     ^ (pos 46: T->G)      ^ (pos 59: C->G)

# Ejecutar análisis
resultados = analizar_variantes(secuencia_wuhan, secuencia_pase10)

# Mostrar resultados en pantalla
print("=== RESULTADOS DEL ANÁLISIS DE VARIANTES ===")
if resultados:
    print(f"Se han detectado {len(resultados)} mutaciones:")
    for m in resultados:
        print(f"• Posición {m['posicion']}: {m['de']} -> {m['a']}")
else:
    print("No se detectaron cambios genómicos.")
