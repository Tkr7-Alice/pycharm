class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado (self):
        return self.lado

    def calcularArea(self):
        return self.lado * self.lado

q = Quadrado(12)

print("Lado atual:", q.retornarLado())  # Saída: 4
print("Área:", q.calcularArea())  # Saída: 16

q.mudarLado(7)
print("Novo lado:", q.retornarLado())  # Saída: 7
print("Nova área:", q.calcularArea())  # Saída: 49
