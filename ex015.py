#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.



d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados com o carro? '))
totalPriceDay = d*60
totalPriceKm = km*0.15

print('O preço a pagar é R${:.2f}\nR${:.2f} pela quantidade de diárias \nR${:.2f} pela quantidade de km rodados '.format(totalPriceDay + totalPriceKm, totalPriceDay, totalPriceKm))
