#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
price = float(input('Digite o preço atual do produto: R$'))
print('Esse produto com desconto custará R${:.2f}'.format(price * 0.95))

