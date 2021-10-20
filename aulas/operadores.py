#nome = input ('Qual o seu nome? ')
#print('Seu nome é {:>20}!'.format(nome))

n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))

soma= n1+n2
multi= n1*n2
sub=n1-n2
div=n1/n2
expo=n1**n2
divint=n1//n2
rest=n1%n2

print('\nA soma é igual a {}\n'
'A multiplicação é igual a {}\n'
'A subtração é igual a {}\n' 
'A divisão é igual a {}\n'
'A Exponenciação é igual a {}\n'
'A divisão inteira é igual a {}\n'
'O Resto da divisão é igual a {}\n'.format(soma,multi,sub,div,expo,divint,rest))