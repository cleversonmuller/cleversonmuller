#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.


n1 = float(input('indique o primero numero:'))
n2 = float(input('informe o segundo numero:'))

print ('selecione uma funcao:')

funcao = int(input('(Soma:1) (Subtracao:2) (Divisao:3) (Multiplicacao:4)'))
resultado = 0
if funcao == 1:
    resultado = n1+n2
    print(f'a soma é {resultado}')

if funcao == 2:
    resultado = n1-n2
    print(f'a Subtracao é {resultado}')

if funcao == 3:
    resultado = n1/n2
    print(f'a Divisao é {resultado}')

if funcao == 4:
    resultado = n1*n2
    print(f'Multiplicacao é {resultado}')

if resultado %2 == 0:
    print(f'O numero {resultado} é PAR ')
else:
    print(f'O numero {resultado} é IMPAR')

resultado %1 == 0
if int(n1/n2) == n1/n2:
    print('numero intero')
else:
    print('numero desimal')

resultado = n1/n2
if int(n1/n2) == n1/n2:
    print('numero positivo')

else:
    print('numero negativo')

