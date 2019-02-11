#coding: utf-8

entr = int(raw_input())
print entr

qtd = [0] * 7
notas = [100, 50, 20, 10, 5, 2, 1]

for i in range(7):
   qtd[i] = entr / notas[i]
   entr = entr % notas[i]

for i in range(7):
   print "%d nota(s) de R$ %d,00" % (qtd[i], notas[i])
