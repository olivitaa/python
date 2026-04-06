def duracion (playlist):
    sumasegundos = 0
    cancion_larga = ""
    cancion_corta = ""

    min = 9999
    max = -1

    for song in playlist:
        dur = song["duration"]
        min,seg = dur.split(":")
        total_cancion = int(min)*60 + int(seg)
        sumasegundos += total_cancion

        if total_cancion > max:
            max = total_cancion
            cancion_larga = song
        if total_cancion < min:
            min = total_cancion
            cancion_corta = song
    minutos = sumasegundos // 60
    segundos = sumasegundos % 60

    return minutos, segundos, cancion_larga, cancion_corta