
def fatorial(numero):
    num = numero
    fat = 1

    if num % 1 != 0 or num < 0:
        return f'O número {num} é inválido. Digite um número inteiro positivo.'
    
    while num > 1:
        fat *= num

        num -= 1
    
    return fat

n = int(input('Digite um número: '))

print(f'{n}! = {fatorial(n)} ')