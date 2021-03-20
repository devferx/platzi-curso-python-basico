objetos = ['Hola', 3, 3.54, True]
print(objetos)

objetos.append(5)
print(objetos)

objetos.pop(0)
print(objetos)

for elemento in objetos:
    print(elemento)


objetos = objetos[::-1]
print(objetos)
