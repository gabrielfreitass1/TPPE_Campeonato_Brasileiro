from utils import determina_resultado


class EstatisticasTime:
    def __init__(self):
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


class Time:
    def __init__(self, nome):
        self.nome = nome
        self._estatisticas = EstatisticasTime()

    @property
    def pontos(self):
        return self._estatisticas.pontos

    @property
    def vitorias(self):
        return self._estatisticas.vitorias

    @property
    def empates(self):
        return self._estatisticas.empates

    @property
    def derrotas(self):
        return self._estatisticas.derrotas

    @property
    def gols_marcados(self):
        return self._estatisticas.gols_marcados

    @property
    def gols_sofridos(self):
        return self._estatisticas.gols_sofridos

    @property
    def saldo_gols(self):
        return self._estatisticas.saldo_gols

    def adicionar_vitoria(self, gols_pro=0, gols_contra=0):
        self._estatisticas.adicionar_vitoria(gols_pro, gols_contra)

    def adicionar_empate(self, gols_pro=0, gols_contra=0):
        self._estatisticas.adicionar_empate(gols_pro, gols_contra)

    def adicionar_derrota(self, gols_pro=0, gols_contra=0):
        self._estatisticas.adicionar_derrota(gols_pro, gols_contra)

    def registrar_resultado(self, gols_pro, gols_contra):
        determina_resultado(self, gols_pro, gols_contra)

    def __repr__(self):
        return (f"{self.nome} - {self.pontos} pts, "
                f"{self.vitorias}V, {self.empates}E, {self.derrotas}D, "
                f"SG {self.saldo_gols}")
