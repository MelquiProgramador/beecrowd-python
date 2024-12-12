X = int(input())
Y = int(input())
soma = 0
if X > Y:
    a = Y
    X = Y
    Y = a
for i in range(Y+1, X):
        if i % 2 == 1:
            soma +=1
print(soma)