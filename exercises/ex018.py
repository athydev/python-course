"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na
tela o nome do escolhido."""
from  random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
nomes = [n1, n2, n3, n4]
print(f'O aluno escolhido foi: {choice(nomes)}')
