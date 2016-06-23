#GabrielMaurilio
#solicite o preço de uma mercadoria e o percentual de desconto.exiba o valor do desconto e o preço a pagar.

mercadoria = int(input("qual e o preço da mercadoria:"))

desconto = int(input("valor desconto:"))

soma = ( mercadoria / 100 * desconto )

print(soma)

soma = (mercadoria - soma )

print (soma)
