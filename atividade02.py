numeros = []
total = sum(numeros)
quantidade = len(numeros)
resposta = 'S'

while resposta == 'S':
    numero = float(input('informe o numero: '))
    numeros.append(numero)
    quantidade = len(numeros)
    print(f'Quantidade de numeros armazenados e: {quantidade:.2f}')

    resposta = input('\nDeseja continuar? [S/N]').upper()

    while resposta != 'S' and resposta != 'N':
        resposta = input('Resposta inválida! Digite S ou N: ').upper()

    if resposta == 'N':
        break
