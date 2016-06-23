n = int(input("digite um numero"))

x = 1
soma = 0

while x != 0:
    x = int(input("digite o numero:"))
    if x == 0:
        break
    soma = soma + x
print(soma)
