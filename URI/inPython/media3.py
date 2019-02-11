#coding: utf-8

enter = input().split()

n1, n2, n3, n4 = enter

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1*2 + n2*3 + n3*4 + n4)/10
print('Media: %.1f' % media)

if media >= 7.0:
	print('Aluno aprovado.')

if media < 5.0:
	print('Aluno reprovado.')

if media < 7.0 and media >= 5.0:
	print('Aluno em exame.')
	exame = float(input())
	print('Nota do exame: {:.1f}'.format(exame))
	media = (media + exame)/2
	
	if media >= 5.0:
		print('Aluno aprovado.')

	else:
		print('Aluno reprovado.')

	print('Media final: {}'.format(media))

