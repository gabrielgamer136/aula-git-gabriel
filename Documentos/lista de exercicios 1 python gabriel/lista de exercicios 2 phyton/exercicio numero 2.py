#Gabriel maurilio
ano = int(input("digite um ano"))
if ano % 4 != 0:
   print ("nao e bissesto")
else:
  if ano % 100 == 0 and not (ano % 400 == 0):
    print("nao e bissesto")
  else:
      print("e bissesto")
    
