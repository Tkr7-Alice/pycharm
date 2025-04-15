def verificar_sinal(numero):
    return 'Positivo' if numero >= 0 else 'Negativo'

print(verificar_sinal(float(input("Digite um número: "))))