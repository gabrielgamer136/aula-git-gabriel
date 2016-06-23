#GabrielMaurilio
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,assim como a quantidade de dias pelos quais o carro foi alugado. calcule o preço a pagar,sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

quantidade = int(input("quantidade de km percorridos"))

dias = int(input("quantidade de dias que foi alugado o carro"))

soma = (quantidade * 60)
print(soma)

soma2 = (dias * 0.15)
print (soma2)

soma3 = (soma + soma2 )

print ("vai pagar:",soma3)
