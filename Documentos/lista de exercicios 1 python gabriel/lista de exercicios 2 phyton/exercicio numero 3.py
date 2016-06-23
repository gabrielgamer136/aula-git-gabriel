#Gabriel Maurilio

peso = int(input("digite o peso de peixes"))
if peso <= 50:
   print("zero")
else:   
 if peso > 50:
     multa = (peso - 50) * 4
     print ("sua multa foi",multa)
