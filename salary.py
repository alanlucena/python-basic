#Algoritmo para ler o salário de um funcionário e calcular seu novo salário com seu aumento

salary=float(input('Informe o salário do funcionário: '))
increase=int(input('Informe o valor do aumento do funcionário em porcento: '))

calc_increase=salary*(increase/100)
new_salary= (salary + calc_increase)

value=print('\nO novo salário do funcionário é: R${}'.format(new_salary))