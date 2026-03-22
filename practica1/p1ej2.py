segundos = int(input("ingrese cantidad de segundos a convertir: "))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60

print ("horas: ", horas)
print ("minutos: ", minutos)
print ("segundos: ", segundos)