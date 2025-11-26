import pytest
from src.gerador_rodadas import gerar_rodadas
from src.time import Time


@pytest.fixture
def times_exemplo():
    return [Time(f"Time{i}") for i in range(1, 21)]


def test_nao_ha_jogos_duplicados(times_exemplo):
    """Verifica que não existem partidas repetidas com mesmo mandante e visitante."""
    rodadas = gerar_rodadas(times_exemplo, seed=2025)
    confrontos = []

    for rodada in rodadas:
        for partida in rodada.partidas:
            confronto = (partida.mandante.nome, partida.visitante.nome)
            confrontos.append(confronto)

    duplicados = [c for c in set(confrontos) if confrontos.count(c) > 1]
    assert not duplicados, f"Há jogos duplicados (mesmo mandante e visitante): {duplicados}"


def test_times_enfrentam_no_maximo_duas_vezes(times_exemplo):
    """Verifica que cada par de times se enfrenta no máximo duas vezes (ida e volta)."""
    rodadas = gerar_rodadas(times_exemplo, seed=2025)
    pares = {}

    for rodada in rodadas:
        for partida in rodada.partidas:
            # Cria um par ordenado, independentemente de quem foi mandante
            par = tuple(sorted([partida.mandante.nome, partida.visitante.nome]))
            pares[par] = pares.get(par, 0) + 1

    repetidos = {p: c for p, c in pares.items() if c > 2}
    assert not repetidos, f"Times que se enfrentaram mais de duas vezes: {repetidos}"


def test_confrontos_invertidos_existem(times_exemplo):
    """Garante que, para cada confronto, o jogo de volta (mandante/visitante trocados) existe."""
    rodadas = gerar_rodadas(times_exemplo, seed=2025)
    confrontos = {(p.mandante.nome, p.visitante.nome) for r in rodadas for p in r.partidas}

    faltando = []
    for mandante, visitante in confrontos:
        if (visitante, mandante) not in confrontos:
            faltando.append((mandante, visitante))

    assert not faltando, f"Faltam jogos de volta para os confrontos: {faltando}"


def test_rodadas_tem_10_jogos_sem_repeticao_de_times(times_exemplo):
    """Verifica que cada rodada tem 10 jogos e nenhum time joga duas vezes na mesma rodada."""
    rodadas = gerar_rodadas(times_exemplo, seed=2025)

    for rodada in rodadas:
        assert len(rodada.partidas) == 10, f"Rodada {rodada.numero} não tem 10 jogos"
        times_rodada = [p.mandante.nome for p in rodada.partidas] + [p.visitante.nome for p in rodada.partidas]
        duplicados = [t for t in set(times_rodada) if times_rodada.count(t) > 1]
        assert not duplicados, f"Time repetido na rodada {rodada.numero}: {duplicados}"
