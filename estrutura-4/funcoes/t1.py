def imprimir_ate_en(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
try:
    numero = int(input("Digite um número inteiro: "))
    imprimir_ate_en(numero)
except ValueError:
    print("Por favor, informe um número válido: ")