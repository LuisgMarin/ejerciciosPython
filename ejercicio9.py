"""" 9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"."""

n = input("Ingrese un entero: ")
integer = int(n)
caracter = input("ingresa un caracter: ")

def generar_n_caracteres(n, caracter):
    return caracter * n

        
print(generar_n_caracteres(integer, caracter))
