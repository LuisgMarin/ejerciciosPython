"""" 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría
que devolver True. """

palabra = input("Es un palindromo?: ")

def es_palindromo(palabra):
    lista = list(palabra)
    lista.reverse()

    palabraInversa = ''.join(lista)
    
    if palabra == palabraInversa:
        return True
    elif palabra != palabraInversa:
        return False
    else:
        print("palabra invalida")

print(es_palindromo(palabra))
