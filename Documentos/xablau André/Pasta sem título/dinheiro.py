a= float(input("digite a quantidade de minutos falados"))
b = a * 0.20
c = a * 0.18
d = a * 0.15
e = a * 0.08
if a < 200:
    print("você gastou : ",b)

if 400 > a > 200:
    print("você gastou : ",c)

if  400 < a < 800:
    print("voce gastou :",d)
    
if a > 800 :
    print("você gastou :",e)
