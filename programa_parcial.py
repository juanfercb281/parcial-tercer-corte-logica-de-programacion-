def inicializar_grupo(equipos):
    grupo = {}


    """
    PJ (Partidos Jugados): Es el total de veces que el equipo ha salido a la cancha a jugar.
    PG (Partidos Ganados): Cuántos de esos partidos terminaron en victoria para el equipo.
    PE (Partidos Empatados): Cuántos partidos terminaron con el mismo número de goles para ambos equipos (por ejemplo, 0-0, 1-1, 2-2).
    PP (Partidos Perdidos): Cuántos partidos terminaron en derrota.
    
    
    
    
    """
    for equipo in equipos:
        grupo[equipo] = {
            "PJ": 0, "PG": 0, "PE": 0, "PP": 0,
            "GF": 0, "GC": 0, "DG": 0, "Pts": 0
        }
    return grupo

def registrar_partido(grupo, equipo1, goles1, equipo2, goles2):
    """Registra el resultado de un partido y actualiza las estadísticas."""
    # Verificar que ambos equipos existan en el grupo
    if equipo1 not in grupo or equipo2 not in grupo:
        print("Error: Uno o ambos equipos no pertenecen a este grupo.")
        return

    # Actualiza partidos jugados y goles
    grupo[equipo1]["PJ"] += 1
    grupo[equipo2]["PJ"] += 1
    grupo[equipo1]["GF"] += goles1
    grupo[equipo1]["GC"] += goles2
    grupo[equipo2]["GF"] += goles2
    grupo[equipo2]["GC"] += goles1

    # Calcular resultado
    if goles1 > goles2:
        grupo[equipo1]["PG"] += 1
        grupo[equipo1]["Pts"] += 3
        grupo[equipo2]["PP"] += 1
    elif goles2 > goles1:
        grupo[equipo2]["PG"] += 1
        grupo[equipo2]["Pts"] += 3
        grupo[equipo1]["PP"] += 1
    else:
        grupo[equipo1]["PE"] += 1
        grupo[equipo1]["Pts"] += 1
        grupo[equipo2]["PE"] += 1
        grupo[equipo2]["Pts"] += 1

    # Recalcular Diferencia de Goles (DG = GF - GC)
    grupo[equipo1]["DG"] = grupo[equipo1]["GF"] - grupo[equipo1]["GC"]
    grupo[equipo2]["DG"] = grupo[equipo2]["GF"] - grupo[equipo2]["GC"]

def mostrar_tabla(grupo):
    # Ordenamos el diccionario: primero por Puntos (Pts) desc, luego por Diferencia de Goles (DG) desc
    equipos_ordenados = sorted(
        grupo.items(),
        key=lambda item: (item[1]["Pts"], item[1]["DG"]),
        reverse=True
    )

    print("\n" + "="*55)
    print(f"{'POS':<4}{'EQUIPO':<15}{'PJ':<4}{'PG':<4}{'PE':<4}{'PP':<4}{'GF':<4}{'GC':<4}{'DG':<4}{'PTS':<4}")
    print("="*55)
    
    for pos, (equipo, stats) in enumerate(equipos_ordenados, start=1):
        print(f"{pos:<4}{equipo:<15}{stats['PJ']:<4}{stats['PG']:<4}{stats['PE']:<4}{stats['PP']:<4}{stats['GF']:<4}{stats['GC']:<4}{stats['DG']:<4}{stats['Pts']:<4}")
    print("="*55)

# --- PRUEBA DEL PROGRAMA ---

# 1. Definimos los equipos del grupo 
lista_equipos = ["Argentina", "Arabia Saudita", "México", "Polonia"]
mi_grupo = inicializar_grupo(lista_equipos)

# 2. Registra los partidos de la fase de grupos
registrar_partido(mi_grupo, "Argentina", 1, "Arabia Saudita", 2)
registrar_partido(mi_grupo, "México", 0, "Polonia", 0)

registrar_partido(mi_grupo, "Argentina", 2, "México", 0)
registrar_partido(mi_grupo, "Polonia", 2, "Arabia Saudita", 0)

registrar_partido(mi_grupo, "Polonia", 0, "Argentina", 2)
registrar_partido(mi_grupo, "Arabia Saudita", 1, "México", 2)

# 3. Mostramos el resultado final de la tabla de posiciones
mostrar_tabla(mi_grupo)