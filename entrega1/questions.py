import random
categorias= {"informatica": [ "python", "programa", "variable"], "colores": ["celeste", "blanco", "azul", "verde"], "materias": ["seminario", "fod","ayed"]}
print("¡Bienvenido al Ahorcado!")
print()
#Iniciar ahorcado
jugar = "s"
jugadas = 0
puntaje=0
#Mostrar categorias disponibles
print ("Categorias: ")
for c in categorias:
    print (" ", c)
#Pedir ingreso de categoria
elegida = input ("Elegir categoria: ")
while elegida not in categorias:
    print ("Categoria invalida")
    elegida = input ("Elegir categoria: ")
listapalabras = random.sample(categorias[elegida],len(categorias[elegida]))
while (jugar == "s" and jugadas < len(listapalabras)):
    word = listapalabras[jugadas]
    jugadas+=1
    guessed = []
    attempts = 6
    print ("---- NUEVA RONDA ----")
    print()
    print ("Puntaje actual: ",puntaje)
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for char in word:
            if char in guessed:
                progress += char + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje+=6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        if len(letter) != 1 or not letter.isalpha():
            print ("Entrada no válida")
            continue
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            puntaje-=1
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje=0
    print ("puntaje: ",puntaje)
    #tengo palabras para seguir jugando?
    if jugadas == len(listapalabras):
        print ("ya no quedan palabras para adivinar")
        break
    #pregunto si quiere jugar otra ronda, y me aseguro que acepte rtas en mayusculas tb
    jugar = input("queres seguir jugando? (s/n): ").lower()
print ("termino el juego!")
print ("puntaje final: ",puntaje)
