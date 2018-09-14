import os

nombrePrevio = "pedro"
name = nombrePrevio

def guardaNombre(nameString):
    filepointer = open("ficheroNombres.txt",'w+')
    filepointer.write(nameString)
    print("Name",name)
    filepointer.close()

def imprimeString():
    cadena = "Hello World"
    for x in cadena:
        print(x)

while name == nombrePrevio:
    name = input("enter name: ")
    if name == nombrePrevio:
        print("name already taken, please choose another one.")
    else:
        print("your  name is ",name)
        guardaNombre(name)

