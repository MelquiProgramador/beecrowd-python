valor = input().split(" ")

A = float(valor[0])
B = float(valor[1])
C = float(valor[2])

if ((A < C + C) and (B < A + C) and (C < A + B)):
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else: 
    area = (A + B) * C / 2
    print(f"Area = {area:.1f}")