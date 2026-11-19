produtos = []

for i in range(3):
    produto = input('informe o nome do produto: ')
    produtos.append(produto) #add na lista produtosss

print(produtos)  #fora do for ele printa no final, se for dentro ele printa a cada iten

    # acesso ao elemento
n = int(input('digite o indice do elemento a acessar: '))
print(produtos[n-1])

# alterando uma lista 'nome de um elemento'
produtos[n-1] = input('informe o nome do outro elemento: ')
print(produtos)

# removendo a lista 
produto_a_remover = input('\n digite o nome do produto a remover: ')
if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print(produtos)

# insert, po(), clear (pesquisar os metodos)



