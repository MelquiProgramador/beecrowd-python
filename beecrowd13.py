pares = 0
impares = 0
positivos = 0
negativos = 0
for valor in range(5):
    valor1 = int(input())
    if valor1 % 2 == 0:
        pares += 1
    if valor1 % 2 ==1:
        impares += 1
    if valor1 > 0:
        positivos += 1
    if valor1 < 0:
        negativos += 1
print(f"{pares} valor(es) par(es)")
print(f"{pares} valor(es) impar(es)")
print(f"{impares} valor(es) positivo(s)")
print(f"{impares} valor(es) negativo(s)")