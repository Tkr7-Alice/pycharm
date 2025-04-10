while True:
    nota = float(input("Digite sua nota: "))
    if 0 <= nota <= 10:
        print("Nota Ok!!")
        break
    else:
        print("Nota inválida. Digite um valor entre 0 e 10.")
