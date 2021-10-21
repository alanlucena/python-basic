#Algoritmo para ler a largura e altura de uma parede para calcular sua área e determinar quantos litros de tinto serão necessários

#Levando em consideração que para cada litro de tinta é possível pintar 2m².

width=float(input('Quantos metros de largura a parede possui?: '))
height=float(input('Quantos metros de largura a parede possui?: '))
area=(width*height)
paint=2
final_value=float(area/paint)

final_result=print('\nA parede possui {}m de largura\n'
'{}m de altura\n'
'{}m² de área\n'
'Para pintar a parede por completo serão necessários {}L de tinta'.format(width,height,area,final_value))