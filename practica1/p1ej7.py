frase=(input("ingrese palabras separadas por espacios")).split()

lista= [palabra for palabra in frase if len(palabra)>3]
print (lista)