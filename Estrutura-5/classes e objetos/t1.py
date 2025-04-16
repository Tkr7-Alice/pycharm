class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor
# Criando uma bola
minha_bola = Bola("branco", 30, "borracha")

# Mostrando a cor atual
print("Cor atual:", minha_bola.mostraCor())  # Saída: branco
# Trocando a cor
minha_bola.trocaCor("azul")

# Mostrando a nova cor
print("Nova cor:", minha_bola.mostraCor())  # Saída: azul
