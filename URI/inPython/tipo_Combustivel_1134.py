#coding: utf-8
a = 0
g = 0
d = 0

while(True):
    x = int(input())
    if x == 4: break;

    if x == 1: a += 1
    if x == 2: g += 1
    if x == 3: d += 1

print("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d" % (a, g, d))
