#Algoritmo para ler um número e mostrar seu antecessor e sucessor na tela

num = int(input('Digite algum número para saber qual seu antecessor e sucessor : '))

n1=num-1
n2=num+1

print('\nNúmero escolhido: {}\n'
'O seu antecessor é {}\n'
'O seu sucessor de é {}\n'.format(num,n1,n2))