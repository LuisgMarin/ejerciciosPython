"""" 4- Escribir una función que tome un carácter y devuelva True si es una vocal, 
de lo contrario devuelve False. """

caracter = input("Ingrese un letra: ")

def es_vocal(caracter):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if caracter in vocales:
        return True
    else:
        return False

es_vocal = es_vocal(caracter)
print(es_vocal)
