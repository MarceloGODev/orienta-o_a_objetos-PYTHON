class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = float(nota)  # Garantindo que a nota seja um número float
