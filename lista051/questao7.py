'''
Desenvolver um programa que apresente todos os números divisíveis por 4 que sejam menores que 200. Para
saber se o número é divisível por 4 será necessário verificar a lógica desta condição com o comando if. Sendo
divisível, mostre-o; não sendo, passe para o próximo passo. A variável que controla o contador deve ser iniciada
com valor 1.
'''

contador = 1

while (contador <= 200):
    if (contador % 4 != 0):
        pass

    else:
      print(f"contador: {contador}")
    contador = contador + 1




