#coding: utf-8

entr = raw_input().split()

num1 = int(entr[0])
num2 = int(entr[1])

if num1 % num2 == 0 or num2 % num1 == 0: print "Sao Multiplos"
else: print "Nao sao Multiplos"
