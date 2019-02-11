#coding: utf-8

atual = float(input())

novo = 0
percentual = 0

if atual <= 400:
	novo = atual*1.15
	percentual = 15

if 400 < atual <= 800:
	novo = atual * 1.12
	percentual = 12

if 800 < atual <= 1200:
	novo = atual * 1.10
	percentual = 10

if 1200 < atual <= 2000:
	novo = atual * 1.07
	percentual = 7

if 2000 < atual:
	novo = atual * 1.04
	percentual = 4

print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:d} %'.format(novo, (novo - atual), percentual))