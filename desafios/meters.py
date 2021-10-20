value= int(input('Informe a quantidade a ser convertida: '))
choice= int(input('Informe a unidade de medida desejada: '))

choice1=(value*100)
choice2=(value*1000)

if choice == 1:
    print('A conversão de metros para centímetros equivale a {}cm\n'.format(choice1))
elif choice == 2:
    print('A conversão de metros para milímetros equivale a {}mm\n'.format(choice2))
else:
    print('Opção inválida!')