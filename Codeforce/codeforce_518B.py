#coding: utf-8

ent1 = raw_input()
ent2 = raw_input()

TAM = 30

minus = ord("a")
maius = ord("A")

minusList1 = [0] * TAM
maiusList1 = [0] * TAM
minusList2 = [0] * TAM
maiusList2 = [0] * TAM

for i in range(len(ent1)):
	if ent1[i].islower(): minusList1[ord(ent1[i]) - minus] += 1
	else: maiusList1[ord(ent1[i]) - maius] += 1

for i in range(len(ent2)):
	if ent2[i].islower(): minusList2[ord(ent2[i]) - minus] += 1
	else: maiusList2[ord(ent2[i]) - maius] += 1

nivel1 = 0
nivel2 = 0


for i in range(TAM):
	casos = min(minusList1[i], minusList2[i])
	nivel1 += casos
	minusList1[i] -= casos
	minusList2[i] -= casos
	
	casos = min(maiusList1[i], maiusList2[i])
	nivel1 += casos
	maiusList1[i] -= casos
	maiusList2[i] -= casos
	
	nivel2 += min(minusList1[i], maiusList2[i])
	nivel2 += min(minusList2[i], maiusList1[i])

print nivel1, nivel2
