def calcular(base, expoente, multiplicador):
    return (base ** expoente) * multiplicador, base + expoente + multiplicador

base = float(input("Base: "))
expoente = float(input("Expoente: "))
multiplicador = float(input("Multiplicador: "))
resultado, soma = calcular(base, expoente, multiplicador)

print(f"Resultado: {resultado}, Soma: {soma}")