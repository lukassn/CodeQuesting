# coding: utf-8
cont = 0
inter = 0
gremio = 0
draws = 0
keep = True
while (keep):

    if new == 2: keep = False
    cont += 1
    gi, gg = list(map(int, input().split()))

    if gi > gg: inter += 1
    elif gi < gg: gremio += 1
    else: draws += 1

    new = input("Novo grenal (1-sim 2-nao)")

print("%d grenais\nInter:%d\nGremio:%d\nEmpates:%d" % (cont, inter, gremio, draws))
if inter > gremio: print("Inter venceu mais\n")
elif inter < gremio: print("Gremio venceu mais\n")
else: print("Nao houve vencedor\n")
