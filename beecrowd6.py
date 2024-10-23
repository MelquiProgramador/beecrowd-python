idades = int(input())
soma = 0
n = 0
while idades >= 0:
    soma = soma + idades
    n = n + 1
    idades = int(input())

print(f"{soma/n:.2f}")