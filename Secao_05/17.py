
h = float(input("Digite o valor da altura (m): "))
base_maior = float(input("Digite o valor da base maior (m): "))
base_menor = float(input("Digite o valor da base menor (m): "))

if base_maior > 0 and base_menor > 0:
    area = ((base_maior + base_menor) * h) / 2
    print(f"A área do trapézio é {area:.2f}m².")
else:
    print("Algum valor foi digitado incorretamente. Por favor, reveja os valores informados.")
