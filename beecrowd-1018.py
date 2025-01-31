# -*- coding: utf-8 -*-

valor = int(input())

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

notasUm = resto // 1

# SAÍDA
print(valor)
print(f"{notasCem:.0f} nota(s) de R$ 100,00")
print(f"{notasCinquenta:.0f} nota(s) de R$ 50,00")
print(f"{notasVinte:.0f} nota(s) de R$ 20,00")
print(f"{notasDez:.0f} nota(s) de R$ 10,00")
print(f"{notasCinco:.0f} nota(s) de R$ 5,00")
print(f"{notasDois:.0f} nota(s) de R$ 2,00")
print(f"{notasUm:.0f} nota(s) de R$ 1,00")
