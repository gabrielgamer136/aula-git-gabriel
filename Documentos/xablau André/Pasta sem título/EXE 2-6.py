salario=int(input("quanto você ganha por hora"))
horas=int(input("quantas horas trabalhadas por mês"))
bruto=salario*horas
print("seu salario bruto e de ",bruto)
imposto=(11/100*bruto)
print("o imposto de renda ira pegar ",imposto)
inss=(8/100*bruto)
print("o INSS ira pegar",inss)
sindicato=(5/100*bruto)
print("o sindicato ira pegar",sindicato)
g=imposto+inss+sindicato
print("o total de imposto sera",g)
total=(((bruto-imposto)-inss)-sindicato)
print("seu salario liquido é de",total)



