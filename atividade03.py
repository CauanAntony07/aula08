numeros = []
ordenado = sorted(numeros)

for i in range(12):
    numero = int(input('informe um numero inteiro: '))
    numeros.append(numero)
    ordenado = sorted(numeros)
print(f'numeros apresentados em ordem crescente: {ordenado}')