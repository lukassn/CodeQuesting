#coding: utf-8

while (True):
    n = int(input())
    if n == 0: break

    s = ""
    for i in range(1, n+1):
        s += str(i) + " "
    print(s[:-1])
