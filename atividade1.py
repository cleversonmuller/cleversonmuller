#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

numero = int(input('informe um numero: '))
resultado = numero %2
if resultado == 0:
    print(f'O numero {numero} é PAR ')
else:
    print(f'O numero {numero} é IMPAR')
