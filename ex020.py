# 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
firstStudent = str(input('Digite o primeiro nome: '))
secondStudent = str(input('Digite o segundo nome: '))
thirdStudent = str(input('Digite o terceiro nome: '))
fourthStudent = str(input('Digite o quarto nome: '))
lista = [firstStudent, secondStudent, thirdStudent, fourthStudent]
shuffle(lista)

print('A ordem de apresentação dos trabalhos será: ')
print(lista)











