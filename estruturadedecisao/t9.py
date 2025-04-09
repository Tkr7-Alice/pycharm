n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

# Estrutura Condicional
if n1 == n2 == n3:
    ordem = [n1, n2, n3]
elif n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        ordem = [n1, n2, n3]
    else:
        ordem = [n1, n3, n2]
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        ordem = [n2, n1, n3]
    else:
        ordem = [n2, n3, n1]
else:
    if n1 >= n2:
        ordem = [n3, n1, n2]
    else:
        ordem = [n3, n2, n1]

print("Números em ordem decrescente:")
for numero in ordem:
    print(numero)

