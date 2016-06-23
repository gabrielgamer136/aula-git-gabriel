#Gabriel maurilio
lado1 = int(input("digite primeiro lado"))

lado2 = int(input("digite segundo lado "))

lado3 = int(input("digite terceiro lado "))

if lado1 != lado2 != lado3 or lado1 > lado2 + lado3 or lado2 > lado3 + lado1 or lado3 > lado1 + lado2:
    print("e um triangulo")
else:
    print("triangulo isoceles")
if lado1 == lado2 == lado3:
    print ("triangulo equilatero")
if lado1 != lado2 != lado3:
    print("triangulo escaleno")

