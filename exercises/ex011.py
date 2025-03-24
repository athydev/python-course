p = float(input('Diga o preço do produto: R$'))
des = p - ( p * 5 / 100)

print(f'Com 5% de desconto o produto irá de R${p:.2f} para R${des:.2f}')
