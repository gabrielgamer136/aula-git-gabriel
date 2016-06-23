#Gabriel Maurilio
#Escreva um programa que leia a quantidade de dias,horas,minutos e segundos do usuário.calcule o total em segundos.

dias = int(input("digite a quantidade de dias"))
horas =int(input("digite a quantidade de horas"))
minutos=int(input("digite a quantidade de minutos"))
segundos=int(input("digite a quantidade de segundos"))
total = int(input(dias *86400 + horas * 3600 + minutos * 60 + segundos))
 
print("soma")
