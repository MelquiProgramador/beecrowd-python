# -*- coding: utf-8 -*-

chaReal = int(input())

suposicoes = input().split(" ")

a = int(suposicoes[0])
b = int(suposicoes[1])
c = int(suposicoes[2])
d = int(suposicoes[3])

for num in range(len(suposicoes)):
    if suposicoes[num] == chaReal:
        total += 1
        