#Algoritmo para ler o preço de um produto e mostrar o seu novo preço com 5% de desconto

#Alterado o valor do desconto para um variável, para que o usuário possa escolher a quantidade do desconto

price=float(input('Informe o preço do produto desejado: '))
discount=int(input('Informe o valor obtido como desconto: '))

new_price=price*(discount/100)

final_price=print('\nO valor do produto com {}%, de desconto é: {}'.format(discount,new_price))