"""" 10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima
un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo
siguiente:
****
*********
******* """
listaInput = input("Ingrese los elementos de la lista separados por coma: ")
lista = listaInput.split(",")

# Convertir los elementos de la lista en enteros
for i in range(len(lista)):
    lista[i] = int(lista[i])
    
# = input("Ingrese un entero: ")
#1lista = [1,2,3,4,5,6,7,8,9,4]

def procedimiento(lista):
    for numero in lista:
        print('*' * numero)
        
print(procedimiento(lista))

