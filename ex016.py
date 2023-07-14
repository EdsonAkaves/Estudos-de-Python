# 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
num = float(input('Digite um número: '))
integerPart = math.trunc(num)
print('O número digitado é {} e a sua parte inteira é {}'.format(num, integerPart))






















