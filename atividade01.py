vendas = []
total = sum(vendas)

for i in range(10):
    venda = float(input('informe o valor da venda: '))
    vendas.append(venda)
    total = sum(vendas)
print(f'O total das vendas e: {total:.2f}')