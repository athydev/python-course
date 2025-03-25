"""Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo."""

import math

angulo = int(input('Digite um angulo: '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f'O seno, cosseno e a tangente de {angulo} correspondem a: \n'
      f'seno: {math.sin(angulo):.2f} radianos e a {seno:.2f} graus \n'
      f'cosseno: {math.cos(angulo):.2f} radianos e a {cosseno:.2f} graus \n'
      f'tangente: {math.tan(angulo):.2f} radianos e a {tangente:.2f} graus')
