#coding: utf-8

vitoria = 0
derrota = 0
empate = 0

ponto_casa = 0
ponto_fora = 0

gol_pro = 0
gol_con = 0

for i in range(10):
   campanha = raw_input()
   if campanha[5] == "c":
      gol_pro += int(campanha[0])
      gol_con += int(campanha[2])
      if int(campanha[0]) > int(campanha[2]):
         vitoria += 1
         ponto_casa += 3
      
      elif int(campanha[0]) == int(campanha[2]):
         empate += 1
         ponto_casa += 1
      
      elif int(campanha[0]) < int(campanha[2]):
         derrota += 1
         ponto_casa += 0

   elif campanha[5] == "f":
      gol_pro += int(campanha[2])
      gol_con += int(campanha[0])
      if int(campanha[0]) < int(campanha[2]):
         vitoria += 1
         ponto_fora += 3
      
      elif int(campanha[0]) == int(campanha[2]):
         empate += 1
         ponto_fora += 1
      
      elif int(campanha[0]) > int(campanha[2]):
         derrota += 1
         ponto_fora += 0
         
print "%iv, %ie, %id" % (vitoria, empate, derrota)
print "pontos: %i" % (ponto_casa+ponto_fora)
print "saldo: %i (%i pro, %i contra)" % (gol_pro - gol_con, gol_pro, gol_con)
print "pontos em casa: %i" % ponto_casa
print "pontos fora: %i" % ponto_fora
