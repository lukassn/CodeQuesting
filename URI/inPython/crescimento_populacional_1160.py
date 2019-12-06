#coding: utf-8

t = int(input())
cont = 0
while(cont < t):
    cont += 1
    n = input().split()
    pa, pb, g1, g2 = int(n[0]), int(n[1]), float(n[2]), float(n[3])
    anos = 0
    while(pa <= pb):
        if anos > 100: break
        anos += 1
        pa += int(pa * (g1/100))
        pb += int(pb * (g2/100))
    if anos > 100: print("Mais de 1 seculo.")
    else:   print("%d anos." % anos)

