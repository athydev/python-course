"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na
tela o nome do escolhido."""

import random

nome = ['Murilo', 'Mateus', 'Julia', 'Ana']
print(f'O aluno escolhido foi: {random.choice(nome)}')
