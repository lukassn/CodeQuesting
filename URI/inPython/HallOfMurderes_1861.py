# coding: utf-8


hall = {}

while True:
   ent = raw_input().split()
   murderer = ent[0]
   dead = ent[1]
   
   if murderer ==  "0" and dead == "0": break

   hall[murderer] = [dead]

   for i in hall:
      if i == murderer:
         hall[i].append(dead)
   
   for i in hall:
      if i == dead:
         del hall[i]

   

   

print "HALL OF MURDERERS"
for i in hall:
   print "%s %d" % (i, len(hall[i]))\
