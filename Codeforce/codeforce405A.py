#coding: utf-8


n = int(raw_input())

columns = [0] * n

cubes = raw_input().split()

for i in range(n):
	columns[i] = int(cubes[i]);
columns = sorted(columns)

for i in columns:
	print i,
