'''
10) Desenvolver um programa que apresente as potências de 3 variando de 0 a 15. Deve ser considerado que
qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. A apresentação deve observar a seguinte
exibição na tela:
3 elevado à 0 = 1
3 elevado à 1 = 3
3 elevado à 2 = 9
(...)
3 elevado à 15 = 14348907
OBS: Tente fazer em uma classe utilizando Math.pow() e em outra classe sem utilizar Math.pow()
'''


import math
cont = 1

while(cont <= 15):
    print(f"{math.pow(cont,3):.0f}.")
    cont = cont + 1


    #Professor, venho informa-lhe que minha pessoa tentou realizar a segunda proposta, mas infelizmente, por meios oficiais, estou incapactidado de realiza-la. Tenha um excelente dia.

