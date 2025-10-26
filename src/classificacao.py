class Classificacao:
    def __init__(self, times):
        self.times = times

    def gerar_tabela(self):
        return sorted(
            self.times,
            key=lambda t: (t.pontos, t.vitorias, t.saldo_gols, t.gols_marcados),
            reverse=True
        )
