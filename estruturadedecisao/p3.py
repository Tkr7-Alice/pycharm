letra = 0

letra = input("Digite um sexo (f ou m): ").lower()

if letra == 'f':
    print("Feminino")
elif letra == 'm':
    print("Masculino")
else:
    print("Sexo inválido")