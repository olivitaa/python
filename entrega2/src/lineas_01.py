def lineas_y_palabras (text):
    lineas = text.splitlines()
    cantlineas = len(lineas)

    totalpalabras = 0
    lineas_info = []

    for line in lineas:
        palabras= line.split()
        cantidad = len(palabras)
        totalpalabras += cantidad
        lineas_info.append((line, cantidad))

    promedio = (round(totalpalabras/cantlineas,2))

    lineas_sobre_promedio = [line for line, cantidad in lineas_info if cantidad > promedio]

    return cantlineas, totalpalabras, promedio, lineas_sobre_promedio