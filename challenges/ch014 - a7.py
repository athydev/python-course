dia = int(input('Dias alugados: '))
km = float(input('Km rodados: '))

pg = (dia * 60) + (km * 0.15)

print(f'Total a pagar: R${pg:.2f}')
