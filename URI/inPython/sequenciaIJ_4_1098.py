#coding: utf-8

'''
	
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
'''
# deve reinicia o j pra 1 e sempre que reiniciar somar 0.2
i = 0
f = 0
de5em5 = 0
while i <= 2:
	j = 1
	
	for c in range(1,4):
		if de5em5 == 5 or de5em5 == 0:
			print('I={:.0f} J={:.0f}'.format(i,j+f))
			
		else:
			print('I={:.1f} J={:.1f}'.format(i,j+f))
		
		j += 1

	i += 0.2
	f += 0.2
	de5em5 += 1
	if de5em5 == 5: 
		de5em5 = 0



