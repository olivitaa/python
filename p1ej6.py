numero = int(input("ingrese numero: "))
#lista1=[]
#lista5=[]
#for i in range (1,numero):
#    if (i%5 == 0):
 #       lista5.append(i)
  #      continue
   # lista1.append(i)


lista1=[i for i in range(1,numero+1) if (i%5 == 0) ]
lista2=[i for i in range (1,numero+1) if (i%5 !=0)]

print ("lista 1: ", lista1)
print ("lista 2: ", lista2)