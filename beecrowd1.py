valor = float(input())

notasCem = valor // 100 #5
resto = valor % 100 #76

notasCinquenta = resto // 50  # 1
resto = resto % 50 #1

notasVinte = resto // 20 # 1 
resto = resto % 20 #26

notasDez = resto // 10
resto = resto % 10 #0

notasCinco = resto // 5
resto = resto % 5 #1

notasDois = resto // 2
resto = resto % 2 #0

moedaUm = resto // 1
resto = resto % 1 

moedaCinquenta = resto // 0.50
resto = resto % 0.50

moedaVinteCinco = resto // 0.25
resto = resto % 0.25

moedaDez = resto // 0.10
resto = resto % 0.10

moedaCinco = resto // 0.05
resto = resto % 0.05

moedaUmcentavo = resto*100

# SAÍDA
print(f"NOTAS:")
print(f"{notasCem:.0f} nota(s) de R$ 100.00")
print(f"{int(notasCinquenta)} nota(s) de R$ 50.00")
print(f"{int(notasVinte)} nota(s) de R$ 20.00")
print(f"{int(notasDez)} nota(s) de R$ 10.00")
print(f"{int(notasCinco)} nota(s) de R$ 5.00")
print(f"{int(notasDois)} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{moedaUm:.0f} moeda(s) de R$ 1.00")
print(f"{moedaCinquenta:.0f} moeda(s) de R$ 0.50")
print(f"{moedaVinteCinco:.0f} moeda(s) de R$ 0.25")
print(f"{moedaDez:.0f} moeda(s) de R$ 0.10")
print(f"{moedaCinco:.0f} moeda(s) de R$ 0.05")
print(f"{moedaUmcentavo:.0f} moeda(s) de R$ 0.01")