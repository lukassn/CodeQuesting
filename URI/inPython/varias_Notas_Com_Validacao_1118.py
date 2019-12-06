# coding: utf-8

keep = True
grades = 0
cont = 0
while (keep):
    grade = float(input())
    if grade >= 0 and grade <= 10:
        cont += 1
        grades += grade

    else: print("nota invalida")

    if cont == 2:
        print("media = %.2f" % (grades/2))
        cont = 0
        grades = 0
        while(True):
            print("novo calculo (1-sim 2-nao)")
            new = float(input())
            if new == 1: break
            elif new == 2:
                keep = False
                break
