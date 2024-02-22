# import random

vetor = []
numero = 0

while True:

    numero = int(input('Digite um número[-1 para encerrar.]: '))

    if numero == -1:
        print('FIM.')
        break
    
    # Se o vetor estiver vazio, vai adicionar o número.
    if len(vetor) == 0:
        vetor.append(numero)
    else:
        posicao = 0
        # Enquanto a posição do número no vetor, for menor que o Tamanho dele
        # Verifica se o número é menor que o vetor daquela posição, se for, insere o número ali e para a iteração.
        # Se não for, posição soma mais 1, pra comparar com o próximo número do vetor.
        while posicao < len(vetor):
            if numero < vetor[posicao]:
                vetor.insert(posicao, numero)
                break
            posicao += 1
        else:
            vetor.append(numero)

    # print(vetor)

print(vetor)
