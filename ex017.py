# 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
oppositeSide = float(input('Qual o comprimento do cateto oposto? '))
adjacentSide = float(input('Qual o comprimento do cateto adjacente? '))
hypotenuse = math.sqrt(pow(oppositeSide, 2) + pow(adjacentSide, 2))
print('A hipotenusa mede {:.2f}'.format(hypotenuse))


'''Outra forma:

from math import hypot
catop = float(input('Qual o comprimento do cateto oposto? '))
catadj = float(input('Qual o comprimento do cateto adjacente? '))
hip = hypot(catop, catadj)
print('A hipotenusa mede {:.2f}'.format(hip))
#h2 = op2 + adj2
'''

















