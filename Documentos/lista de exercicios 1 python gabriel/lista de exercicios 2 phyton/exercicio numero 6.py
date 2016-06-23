#GabrielMaurilio
hora = int(input("quanto voce ganha por hora:"))
numero = int(input("numero de hora que trabalhadas no mes:"))
sb = hora * numero
print ("salario bruto",sb)
ir = sb * 0.11
print("imposto de renda",ir)
inss = 0.08 * sb
print ("inss",inss)
sindicato = 0.05 * sb
print("sindicato",sindicato)
salarioliquido = sb - (ir + inss + sindicato)
print("salario liquido:",salarioliquido)
