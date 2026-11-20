# SETS "conjuntos"
# colecao mutavel
# nao garente ordem
# nao há indice

# criar sets vazios 
dias = set()
dias.add('segunda')
dias.add('terça')

print(dias)


# conjuntos inicializados
frutas = {'maça', 'uva', 'pera', 'laranja'}

print(frutas)
print(type(frutas))


# remover
frutas.remove('uva')
# frutas.discard('uva')
print(frutas)

print(len(frutas))


# # converter lista para sets
# lista = [5, 7, 4, 1, 2, 8, 13, 6]
# conjunto_set = set(lista)

# print(conjunto_set)

numeros = [5, 7, 4, 1, 2, 8, 13, 6, 5, 5, 13, 8, 29]
conjunto = set(numeros)
numeros = list(conjunto) #converte conjunto set para a lista
print(conjunto)