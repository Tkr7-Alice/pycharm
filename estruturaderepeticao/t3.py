nome = input("Nome: ")
while len(nome) <= 3:
    nome = input("Nome (>3 letras): ")

idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade (0-150): "))

salario = float(input("Salário: "))
while salario <= 0:
    salario = float(input("Salário (>0): "))

sexo = input("Sexo (f/m): ").lower()
while sexo not in ['f', 'm']:
    sexo = input("Sexo (f/m): ").lower()

estado = input("Estado civil (s/c/v/d): ").lower()
while estado not in ['s', 'c', 'v', 'd']:
    estado = input("Estado civil (s/c/v/d): ").lower()
