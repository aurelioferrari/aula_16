# criar uma tupla com palavras e identificar as vogais de cada uma delas

lista = ('lapis', "borracha")
for p in lista:
    print(f'\nA palavra {p} tem as vogais:', end = " ")
    for letra in p:
        if letra in "aeiou":
            print(letra, end = " ")

