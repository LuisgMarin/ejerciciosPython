"""1- Definir una función max() que tome como argumento dos números y devuelva el mayor de
ellos. (Es cierto que python tiene una función max() incorporada, pero debe realizarse por
nosotros mismos."""

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(a, b)) 
