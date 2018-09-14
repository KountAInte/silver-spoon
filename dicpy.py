import json
from difflib import get_close_matches
#abro fichero json en una variable de tipo diccionario
data = json.load(open("data.json"))

# funcion que devuelve una palabra 
def traduce(cadena):
    cadena = cadena.lower()
    #busco dentro del diccionario
    if cadena in data:
        return data[cadena]
    elif len(get_close_matches(cadena, data.keys()))>0:
        return "¿Te refieres a %s  ?" % get_close_matches(cadena, data.keys())[0]
    else: 
        return "La palabra no existe."

while True:
#pido input del usuario
    palabra = input("Introduce palabra: ")
    if palabra == 'salir':
        print("Saliendo...")
        break 
        # salgo del bucle en esta linea

#imprime resultado
output = traduce(palabra)
for item in output:
        print(item)

