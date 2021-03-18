#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime.Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
#"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

print('indicador de suspeito')
v1= input('Telefonou para a vítima?')
v2= input('Esteve no local do crime?')
v3= input('Mora perto da vítima?')
v4= input('Devia para a vítima?')
v5= input('Já trabalhou com a vítima?')
funcao = input('se as resposta for  (2*pessoa no crime)  (3* ou 4* cumplice) (5* assasino)  ')
resultado = [v1, v2, v3, v4, v5]

if  resultado == v1:
    print('inocente ')

if  resultado == v2:
    print('pessoa no crime')

if  resultado == v3:
    print('cumplice')
if  resultado == v4:
    print('cumplice')

if resultado == v5:
    print ('assasino')



