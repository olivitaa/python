numero = int(input("ingrese numero: "))
lista1=[]
lista5=[]
for i in range (1,numero):
    if (i%5 == 0):
        lista5.append(i)
        continue
    lista1.append(i)
print("lista 1:") 
for elem in lista1:
    print (elem)
print ("lista con multiplos de 5:")
for elem in lista5:
    print (elem)