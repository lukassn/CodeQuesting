# coding: utf-8

ent = raw_input()

opens = 0
closes = 0

for i in range(len(ent)):
   if ent[i] == ")": closes += 1
   if ent[i] == "(": opens += 1

if opens != closes: print "incorrect"
else: print "correct"
