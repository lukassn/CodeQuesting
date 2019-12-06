# coding: utf-8

def multiplosDe13(i, j):
    multis = []
    cont = 1
    x = 0
    while x <= j:
        if x == cont * 13:
            multis.append(x)
            cont += 1
        x += 1
    return multis


def somaDosMultisDe13(a, i):
    somaDosMultis = 0
    for o in range(len(a)):
        if a[o] >= i:  somaDosMultis += a[o]

    return somaDosMultis

def somaTudo(a, b):
    x = 0
    while a <= b:
        x += a
        a += 1
    return x

a = int(input())
b = int(input())
if a > b: a, b = b, a
x = multiplosDe13(a, b)
print(somaTudo(a, b) - somaDosMultisDe13(x, a))
