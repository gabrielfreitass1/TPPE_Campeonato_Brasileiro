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

    num_times = len(times)
    if num_times % 2 != 0:
        times.append(None)  # caso ímpar

    lista = times[:]
    rodadas = []

    # Gera rodadas de ida
    for rodada_num in range(num_times - 1):
        partidas = []
        for i in range(num_times // 2):
            mandante = lista[i]
            visitante = lista[-(i + 1)]
            if mandante is not None and visitante is not None:
                if rodada_num % 2 == 0:
                    partidas.append(Partida(mandante, visitante))
                else:
                    partidas.append(Partida(visitante, mandante))
        rodadas.append(Rodada(rodada_num + 1, partidas))

        # rotaciona os times
        lista = [lista[0]] + [lista[-1]] + lista[1:-1]

    # Gera retorno
    for i, rodada in enumerate(rodadas.copy(), start=len(rodadas) + 1):
        partidas_invertidas = [Partida(p.visitante, p.mandante) for p in rodada.partidas]
        rodadas.append(Rodada(i, partidas_invertidas))

    return rodadas
