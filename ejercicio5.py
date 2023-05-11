"""" 5- Escribir una funcion sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
devolver 10 y multip([1,2,3,4]) debería devolver 24. """

operacion = input("Ingrese el tipo de operacion: ")

def sum(lista):
    sum = 0
    for elemento in lista:
        sum += elemento
    return sum

def multip(lista):
    multip = 1
    for elemento in lista:
        multip *= elemento
    return multip

lista = [1,2,3,4]

if operacion == "sum":
    print(sum(lista))
elif operacion == "multip":
    print(multip(lista))
else:
    print("operacion invalia")

    

