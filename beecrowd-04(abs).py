# -*- coding: utf-8 -*-
valores = input().split(" ")

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

MaiorAB = (a+b+abs(a-b))/2

if a == MaiorAB:
    MaiorAC = (a+c+abs(a-c))/2
    print(f"{int(MaiorAC)} eh o maior")
else:
    MaiorBC = (b+c+abs(b-c))/2
    print(f"{int(MaiorBC)} eh o maior")