#coding: utf-8

cont = 0
soma = 0
while(True):
    n = int(input())
    if n < 0: break
    else:
        cont += 1
        soma += n
print("%.2f" % (soma/cont))
