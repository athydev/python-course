"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = (co ** 2 + ca ** 2) ** (1/2)
print(f'O comprimento da hipotenusa é: {h1:.2f}')

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é: {hypot(co, ca):.2f}')
