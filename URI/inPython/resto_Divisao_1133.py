#coding: utf-8

a = int(input())
b = int(input())
if a > b: a, b = b, a

c = a+1

while (c < b):
    if c % 5 == 2: print(c)
    if c % 5 == 3: print(c)
    c += 1



