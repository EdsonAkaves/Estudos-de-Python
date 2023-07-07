#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m2.

width = float(input('Digite a largura da parede em metros: '))
height = float(input('Digite a altura da parede em metros: '))
area = width * height
print('Sua parede tem {}m2 de área e para pintar a parede você precisará de {} litros de tinta.'.format(area, area/2))
print('*Cada litro de tinta pinta uma área de 2m2')

