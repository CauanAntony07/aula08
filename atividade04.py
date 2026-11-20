numeros = []

for i in range(15):
    numero = int(input('informe um numero: '))
    numeros.append(numero)

    conjunto = set(numeros)
    numeros = list(conjunto)
print(conjunto)