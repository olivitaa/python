import random
categorias= {"informatica": [ "python", "programa", "variable"], "colores": ["celeste", "blanco", "azul", "verde"], "materias": ["seminario", "fod","ayed"]}
guessed = []
attempts = 6
puntaje=0
print("¡Bienvenido al Ahorcado!")
print()
#Mostrar categorias disponibles
print ("categorias: ")
for c in categorias:
    print (" ", c)
#Pedir ingreso de categoria
elegida = input ("elegir categoria")
while elegida not in categorias:
    print ("categoria invalida")
    elegida = input ("elegir categoria")
word = random.choice(categorias[elegida])
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
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha():
        print ("Entrada no válida")
        print 
        coninue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
        puntaje+=6
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
