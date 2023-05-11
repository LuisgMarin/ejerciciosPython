"""" 8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos
1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle
for anidado. """

lista1_input = input("Ingrese los elementos de la lista separados por coma: ")
lista1 = lista1_input.split(",")
lista2_input = input("Ingrese los elementos de la lista separados por coma: ")
lista2 = lista2_input.split(",")

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
        
print(superposicion(lista1, lista2))
