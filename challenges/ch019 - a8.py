"""O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""
from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segunda nome: ')
n3 = input('Terceira nome: ')
n4 = input('Quarta nome: ')

nome = [n1, n2, n3, n4]
shuffle(nome)

print('A ordem de apresentação será: \n'
      f'Pimeira apresentação: {nome[0]} \n'
      f'Segunda apresentação: {nome[1]} \n'
      f'Terceira apresentação: {nome[2]} \n'
      f'Quarta apresentação: {nome[3]}')
