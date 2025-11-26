import pytest
from src.time import Time
from src.partida import Partida
from src.classificacao import Classificacao
from src.gerador_rodadas import gerar_rodadas

@pytest.fixture
def times_exemplo():
    return [
        Time("Cruzeiro"),
        Time("São Paulo"),
        Time("Santos"),
        Time("Internacional")
    ]

def test_pontuacao_acumulada_em_multiplas_rodadas(times_exemplo):
    cruzeiro, saopaulo, santos, inter = times_exemplo

    Partida(cruzeiro, saopaulo, 2, 0).jogar()
    Partida(santos, inter, 1, 1).jogar()

    assert cruzeiro.pontos == 3
    assert saopaulo.pontos == 0
    assert santos.pontos == 1
    assert inter.pontos == 1

    tabela = Classificacao(times_exemplo).gerar_tabela()
    assert tabela[0].nome == "Cruzeiro"


def test_classificacao_final_turno_e_returno(times_exemplo):
    rodadas = gerar_rodadas(times_exemplo, seed=2025)

    for rodada in rodadas:
        for partida in rodada.partidas:
            partida.jogar()

    tabela_final = Classificacao(times_exemplo).gerar_tabela()

    for t in tabela_final:
        assert t.pontos >= 0

    pontos_ordenados = [t.pontos for t in tabela_final]
    assert pontos_ordenados == sorted(pontos_ordenados, reverse=True)

    campeao = tabela_final[0]
    assert isinstance(campeao.nome, str)
    assert campeao.pontos >= tabela_final[-1].pontos


def test_desempate_por_vitorias_apos_rodadas(times_exemplo):
    """Garante que, em caso de empate em pontos, o critério de vitórias define a posição."""
    cruzeiro, saopaulo, santos, inter = times_exemplo

    cruzeiro.pontos, cruzeiro.vitorias = 6, 2
    saopaulo.pontos, saopaulo.vitorias = 6, 1
    santos.pontos, santos.vitorias = 6, 1
    inter.pontos, inter.vitorias = 6, 1

    tabela = Classificacao(times_exemplo).gerar_tabela()
    assert tabela[0].nome == "Cruzeiro"
