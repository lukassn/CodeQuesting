#coding: utf-8

inicio, fim = map(int, input().split())

tempo = 0

if inicio == fim: tempo = 24

if fim < inicio:
	tempo = 24 - inicio + fim

if inicio < fim:
	tempo = fim - inicio


print('O JOGO DUROU {} HORA(S)'.format(tempo))