"""Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo."""

from  math import radians, sin, cos, tan

angulo = int(input('Digite um angulo: '))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f'O seno, cosseno e a tangente de {angulo} correspondem a: \n'
      f'seno:{seno:.2f} \n'
      f'cosseno:{cosseno:.2f} \n'
      f'tangente:{tangente:.2f}')
