suma = 0

while True:
    precio = float(input("ingresar precio: "))
    if (precio == 0):
        break
    suma += precio
print ("total: $",suma)