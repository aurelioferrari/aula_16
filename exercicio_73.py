# fazer uma tupla com os 20 da tabela do brasileirao
# A) 5 primeiros colocados
# B) ultimos 4 colocados
# C) lista dos times em ordem alfabética
# D) Em qual posição está o Avaí

tabela = ("Corinthians", "Palmeiras", "São Paulo", "Atlético-MG", "Botafogo",
          "Santos", "Fluminense", "Coritiba", "América-MG", "Avaí",
          "Internacional", "Athletico-PR", "Bragantino", "Flamengo", "Goiás",
          "Cuiabá", "Atlético-GO", "Juventude", "Ceará SC", "Fortaleza")
print("Os 5 primeiros colocados são:")
for c in range(0, 5):
    print(tabela[c])
print("\n")

print("Os times na zona de rebaixamento são:")
for t in range(-4, 0, 1):
    print(f"\033[1:31m{tabela[t]}\033[m")
print("\n")

print("Os times em ordem alfabética são:")
print(sorted(tabela))

print(f'O Avaí está na {tabela.index("Avaí")+1} posição.')

