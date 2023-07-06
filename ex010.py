#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere U$1,00 = R$5,28.

d = float(input('Digite quanto você tem na carteira: R$'))
print('Com R${:.2f}, você pode comprar U${:.2f}'.format(d, d/5.28))

