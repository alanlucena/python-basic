#Algoritmo para ler um número e mostrar seu dobro, triplo e raiz quadrada

number = int(input('Escolha o número: '))

double= numero*2
triple= numero*3
expo= numero**0.5

print('\nO número escolhido foi: {}\n'
'O dobro do valor do número escolhido é: {}\n'
'O triplo do valor do número escolhido é {}\n'
'A raiz quadrada do número escolhido é {}\n'.format(number,double,triple,expo))