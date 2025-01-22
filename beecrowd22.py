#Beecrowd - 1072 Aula:  12  (29/08/2022)
valor = input().split()

valor1 = int(valor[0])
valor2 = int(valor[1])
valor3 = int(valor[2])


lista = []
lista.append(valor1)
lista.append(valor2)
lista.append(valor3)


lista1 = lista
lista1.sort()
for i in lista1:
    print(i)

print()
print(valor1)
print(valor2)
print(valor3)