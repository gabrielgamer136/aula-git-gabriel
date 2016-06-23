print("  irei ler em minutos a quantidade de dias, horas, e minutos; Basta você digitar : ")

a = int(input("gigite a quantidade de dias : "))

b = int(input("gigite a quantidade de horas : "))

c = int(input("gigite a quantidade de minutos : "))

diashoras = a * 1440

print("a quantidade de minutos nesses dias é : ",diashoras)

horashoras = b * 60

print("a quantidade de minutos nessas horas é : ",horashoras)

minutoshoras = c * 1

print(" a quntidade de minutos é : ", minutoshoras)

resposta = diashoras+horashoras+minutoshoras

print("a resposta é : ",resposta)

