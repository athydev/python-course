l = float(input('Largura da parede: '))
at = float(input('Altura da parede: '))

a = l * at

print(f'Sua parede tem a dimensão de {l}x{at} e sua área é de {a}m². \n'
      f'Para pintar essa parede, você precisará de {a/2}l de tinta')