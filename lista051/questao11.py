'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();)
'''
n1 = int(input("Insira um número:"))
exp = int(input("Insira um número pra ser o expoente:"))
contador = 1
acumulador = 1
while (contador <= exp):
    acumulador = acumulador * n1
    contador = contador + 1

print(f"{n1} elevado à {exp} = {acumulador}")



