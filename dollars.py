#Algoritmo para ler um valor em reais e informar quantos dólares podem ser comprados com a quantidade de dinheiro em R$

#Levando em consideração a taxa do dólar de R$3,27 -> US$1,00

wallet=float(input('Quantos reais você deseja converter em dólar?: '))
dolar=float(3.27)
convert=float(wallet/dolar)

value=print('O cliente possui: R${}\n'
'O valor base do dólar em real é: R${}\n'
'Com este valor é possível comprar: US${}\n'.format(wallet,dolar,convert))