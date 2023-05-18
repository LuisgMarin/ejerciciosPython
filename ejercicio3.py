""""  Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que
python tiene la función len() incorporada, pero escribirla por nosotros """
input = input("Ingrese una cadena o una lista separada por comas: ")
inputList = input.split(",")

def cadenaOlista(input):
    for elemento in input:
      if elemento == ',':
        print("La longitud de la lista es:", len(inputList))
    else: 
        print("La longitud de la lista es:", len(input))

def len(lista):
    contador = 0
    for elemento in lista:
        contador += 1
    return contador


print(cadenaOlista(input))
