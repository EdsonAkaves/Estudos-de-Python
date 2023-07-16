# 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude. Lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
firstStudent = input('Digite o nome do primeiro aluno: ')
secondeStudent = input('Digite o nome do segundo aluno: ')
thirdStudent = input('Digite o nome do terceiro aluno: ')
fourthStudent = input('Digite o nome do quarto aluno: ')

lista = [firstStudent, secondeStudent, thirdStudent, fourthStudent]
sorteado = choice(lista)
print('O aluno sorteado é {}'.format(sorteado))








