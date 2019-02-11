#coding: utf-8

entr = int(raw_input())
Ox = raw_input().split()

temp = []


for i in range(entr):
   casa = int(Ox[i])
   
   mx = max(abs(casa - int(Ox[0])), abs(casa - int(Ox[-1])))
   
   if i == 0:
      mn = abs(casa - int(Ox[i + 1]))
   
   elif i == entr - 1:
      mn = abs(casa - int(Ox[i - 1]))
   
   else:
      mn = min(abs(casa - int(Ox[i -1])), abs(casa - int(Ox[i + 1])))
   temp.append([mn, mx])

for i in range(len(temp)):
   print "%d %d" % (temp[i][0], temp[i][1])
