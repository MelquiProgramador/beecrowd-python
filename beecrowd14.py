salario = float(input())


entrada = input().split(" ")
codigo = int(entrada[0])
quantidade = int(entrada[1])
precos = [4.00, 4.50, 5.00, 2.00, 1.50]
total = precos[codigo-1] * quantidade
print(f"Total: R$ {total:.2f}")


if salario <= 400.00:
    reajuste = 1.15
    total = reajuste * salario

if salario >= 400.01 and salario <= 800.00:

if salario >= 800.01 and salario <= 1200.00:

if

if

if