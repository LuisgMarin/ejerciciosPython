""""  Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que
python tiene la función len() incorporada, pero escribirla por nosotros """

def len(lista):
    contador = 0
    for elemento in lista:
        contador += 1
    return contador

lista = float(input("Ingrese el número de lista: "))

if lista == 1:
    lista = ["apple", "banana", "cherry"]
else :
    lista = [1,2,3,4,5,6,7,8,9,4]
    

len = len(lista)

print("La longitud de la lista es:", len)
