#coding: utf-8

'''
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

'''

dia0 = input().split('Dia ')
dia0 = int(dia0[1])

hora = input().split(' : ')
hora0 = int(hora[0])
min0 = int(hora[1])
seg0 = int(hora[2])

diaN = input().split('Dia ')
diaN = int(diaN[1])

hora = input().split(' : ')
horaN = int(hora[0])
minN = int(hora[1])
segN = int(hora[2])

dias = diaN - dia0

horas = horaN - hora0
if horas < 0:
	horas += 24
	dias -= 1

minutos = minN - min0
if minutos < 0:
	minutos += 60
	horas -= 1

segundos = segN - seg0
if segundos < 0:
	segundos += 60
	minutos -= 1

print(str(dias) + ' dia(s)')
print(str(horas) + ' hora(s)')
print(str(minutos) + ' minuto(s)')
print(str(segundos) + ' segundo(s)')








