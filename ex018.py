# 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angle = float(input('Digite o valor do ângulo em graus:  '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print('O valor do ângulo é {}, o valor do seu seno é {:.2f}, o valor do seu cosseno é {:.2f} e o valor de sua tangente é {:.2f}'.format(angle, sine, cosine, tangent))















