#coding: utf-8

l = []
cont = 0
while(cont < 20):
    n = int(input())
    l.append(n)
    cont += 1
a = 0
z = len(l)-1
while(a <= len(l)-1):
    print("N[%d] = %d" % (a,l[z]))
    a += 1
    z -= 1
