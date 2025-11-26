from src.gerador_rodadas import *

class Rodada:
    def __init__(self, numero, partidas):
        self.numero = numero
        self.partidas = partidas

    def jogar(self):
        print(f"\n=== Rodada {self.numero} ===")
        for partida in self.partidas:
            partida.jogar()
            print(f"{partida.mandante.nome} {partida.gols_mandante} x {partida.gols_visitante} {partida.visitante.nome}")

def gerar_rodadas(times, seed=None):
    return GeradorDeRodadas(times, seed).executar()
