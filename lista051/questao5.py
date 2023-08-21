'''
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:
Considerando como exemplo o fornecimento do número 2
2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
---------------------------------------------------
N = int(input("Escolha um número"))
print(f"{N} * 1 = {N * 1}")
print(f"{N} * 2 = {N * 2}")
print(f"{N} * 3 = {N * 3}")
print(f"{N} * 4 = {N * 4}")
print(f"{N} * 5 = {N * 5}")
print(f"{N} * 6 = {N * 6}")
print(f"{N} * 7 = {N * 7}")
print(f"{N} * 8 = {N * 8}")
print(f"{N} * 9 = {N * 9}")
print(f"{N} * 10 = {N * 10}")
'''

num = int(input("Informe um número:"))
cont = 1

while(cont <= 10):
    print(f"{num} . {cont} = {num*cont}")
    cont = cont + 1