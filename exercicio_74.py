# gerar 5 números aleatórios e coloca em uma tupla
# mostrar a listagem e indicar o maior e o menor

import random

n1 = (random.randint(1, 100))
menor = n1
maior = n1
n2 = (random.randint(1, 100))
if n2 > maior:
    maior = n2
if n2 < menor:
    n2 = menor
n3 = (random.randint(1, 100))
if n3 > maior:
    maior = n3
if n3 < menor:
    n3 = menor
n4 = (random.randint(1, 100))
if n4 > maior:
    maior = n4
if n4 < menor:
    n4 = menor
n5 = (random.randint(1, 100))
if n5 > maior:
    maior = n5
if n5 < menor:
    n5 = menor
tupla = (n1, n2, n3, n4, n5)

print(tupla)
print("-=" *30)
print(f"O menor valor é: {menor} e o maior valor é: {maior}")