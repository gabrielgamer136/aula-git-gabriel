#GabrielMaurilio
#escreva um  programa para calcular a reduçao do tempo de vida de um fumante.pergunte a quantidade de cigarros fumados por dia e quantos anos ele ja fumou.considere que um fumante per 10 minutos de vida a cada cigarro,calcule quantos dias de vida um fumante perderá.exiba o total de dias.

cigarrosfumados = int(input("quantidade de cigarros fumados por dia:"))
anosquefumou = int(input("quantos anos fumou"))

diasperdidosporcigarro = (0.0069 * cigarrosfumados)

diasperdidosporano = (365 * anosquefumou)

diasperdidos = diasperdidosporcigarro + diasperdidosporano
print (diasperdidos)
