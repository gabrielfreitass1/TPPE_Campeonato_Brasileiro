class Time:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0

    @property
    def saldo_gols(self):
        return self.gols_marcados - self.gols_sofridos

    def adicionar_vitoria(self, gols_pro=0, gols_contra=0):
        self.pontos += 3
        self.vitorias += 1
        self.gols_marcados += gols_pro
        self.gols_sofridos += gols_contra

    def adicionar_empate(self, gols_pro=0, gols_contra=0):
        self.pontos += 1
        self.empates += 1
        self.gols_marcados += gols_pro
        self.gols_sofridos += gols_contra

    def adicionar_derrota(self, gols_pro=0, gols_contra=0):
        self.derrotas += 1
        self.gols_marcados += gols_pro
        self.gols_sofridos += gols_contra

    def registrar_resultado(self, gols_pro, gols_contra):
        if gols_pro > gols_contra:
            self.adicionar_vitoria(gols_pro, gols_contra)
        elif gols_pro == gols_contra:
            self.adicionar_empate(gols_pro, gols_contra)
        else:
            self.adicionar_derrota(gols_pro, gols_contra)

    def __repr__(self):
        return (f"{self.nome} - {self.pontos} pts, "
                f"{self.vitorias}V, {self.empates}E, {self.derrotas}D, "
                f"SG {self.saldo_gols}")