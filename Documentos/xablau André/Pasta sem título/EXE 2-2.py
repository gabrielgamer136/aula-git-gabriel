ano = int(input("qual o ano : "))
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 !=0 :
        print('o ano nao bissexto')
    else:
        print("o ano e bissexto")
else :
    print("o a no e bissexto")
    
