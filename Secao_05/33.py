
preco_antigo = float(input("Digite o preço antigo: "))

if preco_antigo <= 50:
    print(f"O preço novo é: R$ {preco_antigo * 1.05}")
    print('Barato')
elif 50 < preco_antigo <= 100:
    print(f"O preço novo é: R$ {preco_antigo * 1.10}")
    print('Normal')
else:
    print(f"O preço novo é: R$ {preco_antigo * 1.15}")
    if 120 <= preco_antigo < 200:
        print('Caro')
    else:
        print('Muito caro')
