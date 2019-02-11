#coding: utf-8

moves = []

while (True):
   ent = raw_input().split()
   x1 = int(ent[0])
   y1 = int(ent[1])
   x2 = int(ent[2])
   y2 = int(ent[3])
   
   if(x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0): break
    
   if(x1 == x2 and y1 == y2): print("0")
   
   elif((x2-x1) == -(y2-y1) or -(x2-x1) == -(y2-y1) or -(x2-x1) == (y2-y1) or (x2-x1) == (y2-y1)): print("1")
   
   elif(x1 == x2 or y1 == y2): print("1")
   
   else: print("2")
