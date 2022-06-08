# criar uma tupla com nomes de produtos e preços
# mostrar tabela com os produtos e preços

lista = (str(input('Qual o nome do produto? ')), float(input('Quanto ele custa? ')),
         str(input('Qual o nome do produto? ')), float(input('Quanto ele custa? ')),
         str(input('Qual o nome do produto? ')), float(input('Quanto ele custa? ')),
         str(input('Qual o nome do produto? ')), float(input('Quanto ele custa? ')))

for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}: R$', end="")
    if item % 2 != 0:
        print(f'{lista[item]:>5}')


