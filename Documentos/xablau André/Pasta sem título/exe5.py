print("vamos clacular o desconto de uma mercadoria")

a= int(input("digite o preço da mercadoria"))
b= int(input("digite o percentual de desconto"))
percentual = a/100 * b
mercadoria = a - percentual
print("o desconto é de :", percentual)
print("o valor a se pagar é :", mercadoria)

