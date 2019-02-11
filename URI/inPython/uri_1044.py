# coding: utf-8

ent1 = raw_input().split()
num1 = int(ent1[0])
num2 = int(ent1[1])

if num2 % num1 == 0 or num1 % num2 == 0:
	print "Sao Multiplos"
	
else: print "Nao sao Multiplos"
