

cont_pares = cont_lidos = 0

while True:
    numero = int(
        input('Digite um número inteiro [Para encerrar digite 1000]: '))
    cont_lidos += 1
    if numero == 1000:
        print('Fim.')
        break
    if numero % 2 == 0:
        cont_pares += 1
