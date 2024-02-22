

def verifica_numero(numero):
    
    if numero >= 0:
        if (numero**0.5) % 1 == 0:
            resultado = f'SIM, {numero} é quadrado perfeito.'
        else:
            resultado = f'NÂO, {numero} não é quadrado perfeito.'

        return resultado
    else:
        resultado = 'Número inválido.'

n = int(input('Digite um número inteiro que deseja verificar se é ou não quadrado perfeito: '))

print(verifica_numero(n))