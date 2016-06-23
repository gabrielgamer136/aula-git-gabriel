#GabrielMaurilio
m = int(input("quantos metros"))
litros = m / 3
if litros / 18 == 0:
 latas = litros / 18
else:
 latas= int(litros / 18) + 1
pagar = latas * 80
print("total a pagar",pagar)
print("total em latas",latas)

