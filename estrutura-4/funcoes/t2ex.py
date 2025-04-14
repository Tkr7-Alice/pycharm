def imprimir(numero):
    parada_i = numero + 1
    resposta = ""

    for i in range(1, parada_i):
        parada_j = i + 1
        for j in range(1, parada_j):
            resposta += str(j) + ""
        resposta += "\n"
    return resposta
# x = int(print("Informe um número maior que 0: ")
#print(imprimir(x))
print(imprimir(5))
