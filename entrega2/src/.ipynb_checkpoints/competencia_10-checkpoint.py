#inicializacion de tabla de resultados, guardo una clave extra "rondas" para saber la cantidad de rondas que jugo cada cocinero y asi calcular el promedio al final
def inicializar_tabla(nombres):
    tabla = []
    for nom in nombres:
        tabla.append({
            'Cocinero': nom,
            'Puntaje': 0,
            'Rondas ganadas': 0,
            'Mejor ronda': 0,
            'Rondas': 0
        })
    return tabla 

#calculo de puntaje por ronda

def puntaje_ronda(jueces):
    total = 0
    for juez in jueces:
        total += jueces[juez]  
    return total

def imprimir_ranking_ronda(resultados):
    text = ""
    puesto = 1
    for res in resultados:
        text += (f"{puesto}: {res[0]} - ({res[1]} pts) \n")
        puesto += 1
    return text

def actualizar_tabla(tabla,puntaje,nom_cocinero):
    for jugador in tabla:
        if jugador["Cocinero"] == nom_cocinero:
            jugador["Puntaje"] += puntaje
            jugador["Rondas"] += 1
            if puntaje > jugador["Mejor ronda"]:
                jugador["Mejor ronda"] = puntaje

def ronda_ganada(tabla,nom_ganador):
    for jugador in tabla:
        if jugador["Cocinero"] == nom_ganador:
            jugador["Rondas ganadas"] += 1

def imprimir_tabla_final(tabla):
    tabla.sort(key=lambda x: x['Puntaje'], reverse=True)
    print ("Cocinero  |  Puntaje  |  Rondas ganadas  |  Mejor ronda  |  Promedio")

    #agrego linea para que quede mas estetico
    print ("-"*70)

    for jugador in tabla:
        #calculo promedio antes de imprimir
        promedio = round(jugador["Puntaje"]/jugador["Rondas"],2) 
        print (f"{jugador['Cocinero']}       {jugador['Puntaje']}      {jugador['Rondas ganadas']}      {jugador['Mejor ronda']} {promedio}")
    print ("-"*70)

def competencia_cocina(rounds):
    nombres_cocineros = list(rounds[0]["scores"].keys())
    tabla = inicializar_tabla(nombres_cocineros)
    numero_ronda = 1

    for ronda in rounds:
        tema = ronda["theme"]
        puntaje = ronda["scores"]
        print(f"Ronda {numero_ronda} - {tema}:")
        numero_ronda += 1
        #donde guardo los resultados de la ronda
        res_ronda = []
        #recorro actualizando la tabla y guardando los resultados de la ronda
        for nom,jueces in ronda["scores"].items():
            puntos = puntaje_ronda(jueces)

            res_ronda.append([nom,puntos])
            actualizar_tabla(tabla,puntos,nom)
        #ordenar resultados de forma descendente 
        
        res_ronda.sort(key=lambda x: x[1], reverse=True)
        ganador = res_ronda[0][0] #el que quedo primero

        print (f"Ganador: {ganador} ({res_ronda[0][1]} pts)")
        print(imprimir_ranking_ronda(res_ronda))
        ronda_ganada(tabla,ganador)
    print ("Tabla final:")
    imprimir_tabla_final(tabla)