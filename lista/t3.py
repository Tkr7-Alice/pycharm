vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    numero = int(input(f"Vetor 1 - Digite o {i+1}º número: "))
    vetor1.append(numero)

for i in range(10):
    numero = int(input(f"Vetor 2 - Digite o {i+1}º número: "))
    vetor2.append(numero)

vetor3 = vetor1 + vetor2

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor 3 (junção dos dois):", vetor3)

