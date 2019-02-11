#coding: utf-8

enter = input().split()
code = int(enter[0])
qtd = int(enter[1])

cardapio = []

cardapio.append(4.0000)
cardapio.append(4.5000)
cardapio.append(5.0000)
cardapio.append(2.0000)
cardapio.append(1.5000)

print("Total: R$ %.2f" % (cardapio[code-1]*qtd))