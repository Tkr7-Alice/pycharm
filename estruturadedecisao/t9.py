n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

numeros = [n1, n2, n3]  # cria a lista com os 3 números

numeros.sort(reverse=True)  # ordena em ordem decrescente

print("Números em ordem decrescente:", numeros)

