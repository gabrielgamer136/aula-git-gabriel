#9

numero=0
soma=0
total_n=0
media=0
float (media)

while (numero>=0):
    numero=int(input("Informe um número: "))
    soma=(soma+numero)
    total_n=total_n+1
    media=soma/total_n
    print ("Resultado soma: %d" %soma)
    print ("Resultado media: %.2f" %media)
    print ("Foram adicionados %d valores" %total_n)
    if (numero<0):
        break
    
        
