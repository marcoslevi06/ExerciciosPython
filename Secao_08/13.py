

def operacao(numero1, numero2, sinal):

    if sinal == '+':
        N = numero1 + numero2
    elif sinal == '/':
        N = numero1 / numero2
    elif sinal == '*':
        N = numero1 * numero2
    else:
        N = 'Valor inválido.'

    return N


n1 = float(input('Digite primeiro número: '))
n2 = float(input('Digite o segundo número: '))
operador = input('Digite o sinal da operação: [*] Multiplicação - [+] Soma - [/] Divisão: ')


print(operacao(numero1=n1, numero2=n2, sinal=operador))