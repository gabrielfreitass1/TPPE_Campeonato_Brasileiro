from src.partida import Partida
import random

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
    if seed is not None:
        random.seed(seed)

    rodadas = []
    num_times = len(times)

    partidas = []
    for i in range(num_times):
        for j in range(i + 1, num_times):
            partidas.append(Partida(times[i], times[j]))
            partidas.append(Partida(times[j], times[i]))

    random.shuffle(partidas)

    jogos_por_rodada = num_times//2
    numero_rodada = 1
    
    for i in range(0, len(partidas), jogos_por_rodada):
        rodadas.append(Rodada(numero_rodada, partidas[i:i + jogos_por_rodada]))
        numero_rodada += 1

    return rodadas
