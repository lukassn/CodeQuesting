#coding: utf-8

from fractions import Fraction
primeira_entrada = int(raw_input())


l = []
for i in range(primeira_entrada):
   l.append(raw_input().split())


s = []
for i in l:
   N1 = int(i[0])
   N2 = int(i[4])
   D1 = int(i[2])
   D2 = int(i[6])

   if i[3] == '+':
      N = (N1 * D2 + N2 * D1)
      D = (D1 * D2)
      s.append((N,D))
   
   elif i[3] == '-':
      N = (N1 * D2 - N2 * D1)
      D = (D1 * D2)
      s.append((N,D))
   
   elif i[3] == '*':
      N = (N1 * N2)
      D =(D1 * D2)
      s.append((N,D))
   elif i[3] == '/':
      N = (N1 * D2)
      D = (N2 * D1)
      s.append((N,D))
   
saida = []
for i in s:
   N = i[0]
   D = i[1]
   saida.append(("%d/%d = %s") % (N, D, Fraction(N,D)))
   
for i in saida :
   print i\
   
   
   
