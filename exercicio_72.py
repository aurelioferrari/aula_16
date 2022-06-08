# criar uma tupla com contagem por extenso de 0 a 20
# receber um número e mostrar ele por extenso

extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quartorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    numero = int(input("Digite um número de 0 a 20: "))
    while numero < 0 or numero > 20:
        numero = int(input("Digite um número de 0 a 20: "))
    print(extenso[numero])
    opcao = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    while opcao not in "Ss" and opcao not in "Nn":
        opcao = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if opcao in "Nn":
        break

