#coding: utf-8

ent = raw_input()

l = []
vogais = ['a', 'e', 'i', 'o', 'u', 'y']

for i in ent:
   i = i.lower()
   if not(i in vogais):
      l.append('.')
      l.append(i)

saida = ""

for i in l:
   saida += i
   
print saida
