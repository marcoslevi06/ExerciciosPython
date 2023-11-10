

numero = int(input(
    'Digite um número para verificar o menor múltiplo dos positivos até chegar nele: '))

achei_divisor = False
menor_multiplo_comum = 0

while achei_divisor is False:

    menor_multiplo_comum += 1

    for i in range(1, numero + 1):
        # Ex: Imagine a iteração a partir do MMC 2.
        # 1ª: O resto da divisão de 2 pra 1 é diferente de zero? Não. Então é É UM DIVISOR 1.
        # 2ª O resto da divisão de 2 pra 2 é diferente de zero? Não. Então é DIVISOR de 2.
        # 3ª: O resto da divisã de 2 pra 3 é diferente de zero? SIM. Entao 2 não é divisor de 3, passe pro próximo número.

        # Verifca se o MMC é diferente de algum dos números de 1 até o número informado, se algum deles for
        # diferente de zero, significa que ele não é divisor, então pode passar pro próximo número (break.)
        if menor_multiplo_comum % i != 0:
            achei_divisor = False
            break
        else:
            divisor = True

print(
    f"O menor múltiplo comum dos positivos até {numero} é: {menor_multiplo_comum}")
