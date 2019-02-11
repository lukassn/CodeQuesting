#coding: utf-8


def search(numbers, comprimento, value):
   saida = 0
   for k in range(comprimento):
      if numbers[k] == value:
         saida = k + 1
         break
   return saida

cases = 0

while True:
   
   ent = raw_input().split()
   N = int(ent[0])
   Q = int(ent[1])
   Ns = [0] * N
   
   if (N == 0 and Q == 0): break
   else: cases += 1
   
   for i in range(N):
      x = int(raw_input())
      Ns[i] = x
   
   Ns = sorted(Ns)
   
   
   for k in range(Q):
          x = int(raw_input())
          a = search(Ns, N, x)
          
          print "CASE# %d:" % cases
          
          if (a == 0):
              print "%d not found" % x

          else:
              print "%d found at %d" % (x, a)

// guarda a localizacao em negativo e faz um for fora do loop

for y in range(4):
linha = []
for x in range(4):
linha.append(0)
m.append(linha)
