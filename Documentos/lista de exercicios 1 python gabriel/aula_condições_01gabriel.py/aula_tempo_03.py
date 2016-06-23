tempo = int(input("quantos minutos voce usou?"))
if tempo < 200:
   print (tempo * 0.20)
if tempo >= 200 and tempo < 400:
   print (tempo * 0.18)
if tempo > 400 and tempo < 800:
   print(tempo * 0.15)
if tempo >= 800:
   print(tempo * 0.08)
9
