"""" 6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse """

palabra = input("Ingrese una palabra: ")

def inversa(palabra):
    palabra = list(palabra)
    palabra.reverse()
    palabra = ''.join(palabra)
    return palabra

print(inversa(palabra))
