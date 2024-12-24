# beecrowd - 1133     Aula: 29/08/2022

X = int(input())  #programa lê dois valores
Y = int(input())

if X > Y:         # Se o primeiro valor for maior que o segundo
    X, Y = Y, X   # Inverte os valores de X e Y para que a contagem ocorra normalmente na ordem Crescente

for i in range(X + 1, Y):
    if (i % 5) == 2 or (i % 5) == 3:
        print(i)