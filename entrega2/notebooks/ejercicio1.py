text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

lineas = text.splitlines()
cantlineas = len(lineas)
print (f"cantidad de lineas: {cantlineas}")

cantpalabras = 0

for line in lineas:
    palabras= line.split()
    cantpalabras += len(palabras)
print (f"cantidad de palabras: {cantpalabras}")

promedio = (round(cantpalabras/cantlineas,2))
print(f"promedio de palabras por linea: {promedio}")

print (f"lineas por encima del promedio {promedio} : ")
for line in lineas:
    palabras = line.split()
    cantpalabras = len(palabras)
    if (cantpalabras>promedio):
        print (f" \" {line} \" ({cantpalabras} palabras)")
    