preco1 = float(input("Preço 1: "))
preco2 = float(input("Preço 2: "))
preco3 = float(input("Preço 3: "))

menor_preco = min(preco1, preco2, preco3)

print(f"Você deve comprar o produto que custa R${menor_preco:.2f}")

