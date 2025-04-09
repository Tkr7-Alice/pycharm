turno = input("Qual turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ")

if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Valor inválido! Use M, V ou N.")
