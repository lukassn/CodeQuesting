# coding: utf-8

ent = raw_input().split()
n = int(ent[0])
m = int(ent[1])

i = n
if n > m:
     i = m;

if i % 2 == 0:
   print "Malvika"

else:
   print "Akshat"
