from src.partida import Partida
import random
from src.rodada import Rodada

class GeradorDeRodadas:
    def __init__(self, times, seed=None):
        self.times_originais = times
        self.seed = seed
        
        # Variáveis internas para o processamento
        self.lista_times = []
        self.rodadas = []
        self.num_times = 0

    def _preparar_times(self):
        """Ajusta a lista de times para o algoritmo de Round-Robin (inclui 'None' se ímpar)."""
        if self.seed is not None:
            random.seed(self.seed)

        self.num_times = len(self.times_originais)
        self.lista_times = self.times_originais[:]
        
        # Adiciona um time fantasma (None) se a quantidade for ímpar
        if self.num_times % 2 != 0:
            self.lista_times.append(None)
            self.num_times += 1 # Atualiza o número de times (incluindo o None)

    def _gerar_rodadas_ida(self):
        """Gera a primeira metade das rodadas (jogos de ida)."""
        
        # O loop roda N-1 vezes, onde N é o número de times (mesmo com o fantasma)
        for rodada_num in range(self.num_times - 1):
            partidas = []
            
            # Gera as partidas para a rodada atual
            for i in range(self.num_times // 2):
                mandante = self.lista_times[i]
                visitante = self.lista_times[-(i + 1)]
                
                # Ignora partidas com o time fantasma (None)
                if mandante is not None and visitante is not None:
                    # Determina quem joga em casa para balancear
                    if rodada_num % 2 == 0:
                        partidas.append(Partida(mandante, visitante))
                    else:
                        partidas.append(Partida(visitante, mandante))
                        
            self.rodadas.append(Rodada(rodada_num + 1, partidas))

            # Rotaciona os times (o primeiro time da lista (fixo) e o restante)
            self.lista_times = [self.lista_times[0]] + [self.lista_times[-1]] + self.lista_times[1:-1]

    def _gerar_rodadas_volta(self):
        """Gera a segunda metade das rodadas (jogos de volta), invertendo as partidas de ida."""
        
        # Copia as rodadas de ida para evitar modificar a lista durante a iteração
        rodadas_ida_copia = self.rodadas.copy()
        numero_rodada_inicial = len(self.rodadas) + 1
        
        # Itera sobre a cópia e inverte as partidas
        for i, rodada in enumerate(rodadas_ida_copia, start=numero_rodada_inicial):
            partidas_invertidas = [Partida(p.visitante, p.mandante) for p in rodada.partidas]
            self.rodadas.append(Rodada(i, partidas_invertidas))

    def executar(self):
        """Método principal para executar a geração de rodadas."""
        self._preparar_times()
        self._gerar_rodadas_ida()
        self._gerar_rodadas_volta()
        return self.rodadas
