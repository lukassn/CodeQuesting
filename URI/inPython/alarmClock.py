#coding: utf-8

while True:
    H1, M1, H2 , M2 = map(int, raw_input().split())
    
    if H1 == M1 == H2 == M2 == 0: break
    
    else:
      dorme = H1*60 + M1
      acorda = H2*60 + M2
      
      if(acorda <= dorme):
        acorda += 24*60
      
      print(abs(acorda - dorme))
