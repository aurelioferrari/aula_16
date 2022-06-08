import random

numeros = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
           random.randint(1, 100), random.randint(1, 100))
for n in numeros:
    print(f"O número sorteado foi: {n}")
print(f"O maior número é: {max(numeros)}")
print(f"O menor número é: {min(numeros)}")