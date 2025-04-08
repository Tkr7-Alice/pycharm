n1 = 0
n2 = 0
n3 = 0
n1 = float(input("Primeiro número:"))
n2 = float(input("Segundo número:"))
n3 = float(input("Terceiro número:"))
if (n1 == n2) and (n1 == n3):
    print('Os números são iguais')
elif (n1 > n2) and (n1 > n3):
    print(n1, "O maior é o número")
elif (n2 > n3):
    print(n2, "O maior é o número")
else:
    print(n3, "O maior é o número")