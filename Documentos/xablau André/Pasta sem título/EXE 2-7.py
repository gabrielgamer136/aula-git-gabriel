mq=float(input("quantos metros você quer pintar"))
qt=mq/3
dql =qt%18
if dql==0 :
    ql = qt/18
else:
    ql=((qt-dql)/18)+1
print("devera usar",ql)
print("e pagara",(ql*80))
