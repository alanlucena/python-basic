#Algoritmo para ler o nome e duas notas de um aluno e informar sua média

#Plus: Informar se o aluno foi aprovado ou reprovado

name= input('\nInforme o nome do aluno(a): ')
note1= float(input('Informe a primeira nota do aluno(a): '))
note2= float(input('Informe a segunda nota do aluno(a): '))

average=(note1+note2)/2

if average > 6:
    status= 'Aprovado'
else:
    status= 'Reprovado'

print('A média do aluno(a): {} é: {}\n'
'A situação do aluno(a) é: {}\n'.format(name,average,status))