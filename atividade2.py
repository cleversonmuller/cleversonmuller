#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#Dica: utilize uma função de arredondamento.

num = float(input('informe um numero: '))
if int(num) == num:
    print('numero intero')
else:
    print('numero desimal')