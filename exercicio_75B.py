# ler 4 valores e guardar em uma tupla
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os numeros pares

numero = (int(input("Digite um número: ")), int(input("Digite um número: ")),
          int(input("Digite um número: ")), int(input("Digite um número: ")))
print(f'Você digitou os números: {numero}')
print(f'O valor 9 aparceceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares digitados foram: ', end = '')
for n in numero:
    if n % 2 == 0:
        print(n, end = ' ')
