import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)
e = random.randint(1, 100)
f = random.randint(1, 100)
g = random.randint(1, 100)
h = random.randint(1, 100)
i = random.randint(1, 100)
j = random.randint(1, 100)

soma_1 = a + b
soma_2 = c + d
soma_3 = e + f
soma_4 = g + h
soma_5 = i + j

cont_acertos = 0

resp1 = int(input(f'Quanto é {a} + {b} = '))
cont_acertos += 1 if resp1 == soma_1 else 0
print(f'Soma correta para a pergunta 1 = {soma_1}')

resp2 = int(input(f'Quanto é {c} + {d} = '))
cont_acertos += 1 if resp2 == soma_2 else 0
print(f'Soma correta para a pergunta 2 = {soma_2}')

resp3 = int(input(f'Quanto é {e} + {f} = '))
cont_acertos += 1 if resp3 == soma_3 else 0
print(f'Soma correta para a pergunta 3 = {soma_3}')

resp4 = int(input(f'Quanto é {g} + {h} = '))
cont_acertos += 1 if resp4 == soma_4 else 0
print(f'Soma correta para a pergunta 4 = {soma_4}')

resp5 = int(input(f'Quanto é {i} + {j} = '))
cont_acertos += 1 if resp5 == soma_5 else 0
print(f'Soma correta para a pergunta 5 = {soma_5}')


print(f'Ao todo você acertou {cont_acertos} questões! ')
