#coding: utf-8

while (True):

   k = int(raw_input())

   if k == 0: break

   ent = raw_input().split()
   n = int(ent[0])
   m = int(ent[1])

   for i in range(k):
      ent2 = raw_input().split()
      x = int(ent2[0])
      y = int(ent2[1])

      if(x==n or x==m or y==n or y==m): print "divisa"

      elif(x>n and y >m): print "NE"

      elif(x<n and y>m): print "NO"

      elif(x<n and y<m): print "SO"

      elif(x>n and y<m): print "SE"
