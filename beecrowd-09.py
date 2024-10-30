valores = input().split(" ")

for num in range(len(valores)):
    valores[num] = float(valores[num])
valores.sort(reverse=True)

A = valores[0]
B = valores[1]
C = valores[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
if (A**2) == (B**2) + (C**2):
    print("TRIANGULO RETANGULO")
if (A**2) > (B**2) + (C**2) and not (A >= B + C):
    print("TRIANGULO OBTUSANGULO")
if (A**2) < (B**2) + (C**2):
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
if (A == B or A == C or B == C) and not (A==B==C):
    print("TRIANGULO ISOSCELES")