#Escreva um programa que converta uma temperatura digitada em ºC para ºF.

celsius = float(input('Digite uma temperatura em C: '))
print('{}ºC corresponde a {:.1f}F'.format(celsius, 1.8 * celsius + 32))


