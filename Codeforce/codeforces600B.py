# -*- coding: utf-8 -*-

n, m = map(int, (raw_input().split()))

o = [0] * m

p = map(int, raw_input().split())
s = map(int, raw_input().split())

for i in range(m):
   for j in range(n):
      if p[j] <= s[i]: 
         o[i] += 1

for i in o: print i,
