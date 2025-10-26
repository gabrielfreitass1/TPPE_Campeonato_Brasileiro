import random

class Partida:
    def __init__(self, mandante, visitante, gols_mandante=None, gols_visitante=None):
        self.mandante = mandante
        self.visitante = visitante
        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante

    def jogar(self):
        if self.gols_mandante is None or self.gols_visitante is None:
            self.gols_mandante = random.randint(0, 4)
            self.gols_visitante = random.randint(0, 4)

        self.mandante.registrar_resultado(self.gols_mandante, self.gols_visitante)
        self.visitante.registrar_resultado(self.gols_visitante, self.gols_mandante)