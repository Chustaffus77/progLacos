'''
Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente
'''

contador = 0
acumulador = 1

while (contador <= 15):
    print(acumulador)
    acumulador = (contador - 1)+(contador - 2)
    contador = contador + 1

