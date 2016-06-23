print('vamos descobrir se o tiângulo é : ')
a=int(input('digite a medida do primeiro lado'))
b=int(input('digite a medida do segundo lado'))
c=int(input('digite a medida do terceiro lado'))

if a+b>c>a-b:
    print('É um triâgulo' )
    if (a)==(b)==(c) :
        print("o triangulo sera equilatero")

    if (a)==(b) !=c or (a) == (c) !=(b) or (c) == (b) !=(a) :
        print("o triângulo sera isoceles ")

    if (a) != (b) !=(c) :
        print("o triângulo sera escaleno ")

else :
          print("não sera um triangulo")
          
          
