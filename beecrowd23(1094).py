#Beecrowd - 1072 Aula:  12  (29/08/2022) 

N = int(input())
cont, rato, sapo, coelho = 0, 0, 0, 0
for i in range(N):
    quantia, tipo = input().split()
    cont += int(quantia)
    if tipo == "C":
        coelho =+ int(quantia)
    elif tipo == "R":
        rato += int(quantia)
    elif tipo == 'S':
        sapo += int(quantia)

print(f"Total: {cont} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {float((100*coelho)/cont):.2f}%")
print(f"Percentual de ratos: {float((100*rato)/cont):.2f}%")
print(f"Percentual de sapos: {float((100*sapo)/cont):.2f}%")