#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo prinitivo e todas as informações possíveis sobre ele:

info = input('Digite algo: ')
print('É numérico? ', info.isnumeric())
print('É alfanumérico? ', info.isalnum())
print('É alfabético? ', info.isalpha())
print('É decimal? ', info.isdecimal())
print('É maiúsculo? ', info.isupper())
print('É minúsculo? ', info.islower())
print('É somente espaços? ', info.isspace())
print('Está capitalizada? ', info.istitle())
print('Tipo primitivo: ', type(info))




