import pytest
from src.rodada import gerar_rodadas

# Quantidade de time - rodaddas esperadas
parametros = [
    (2, 2),   # 2 times -> 2 rodadas
    (3, 4),   # 3 times -> 4 rodadas
    (4, 6),   # 4 times -> 6 rodadas
    (5, 8),   # 5 times -> 8 rodadas
    (6, 10),  # 6 times -> 10 rodadas
    (20, 38), # 20 times -> 38 rodadas
]

@pytest.mark.funcional
@pytest.mark.parametrize("qtd_times, rodadas_esperadas", parametros)
def test_qtd_rodadas(qtd_times, rodadas_esperadas):
    times = [f"Time {i+1}" for i in range(qtd_times)]
    rodadas = gerar_rodadas(times)

    assert len(rodadas) == rodadas_esperadas, (
        f"Esperado {rodadas_esperadas} rodadas, mas gerou {len(rodadas)}."
    )

@pytest.mark.funcional
@pytest.mark.parametrize("qtd_times", [4, 6, 8, 20])
def test_todos_times_se_enfrentam_duas_vezes(qtd_times):
    times = [f"Time {i+1}" for i in range(qtd_times)]
    rodadas = gerar_rodadas(times)

    confrontos = {}

    for rodada in rodadas:
        for partida in rodada.partidas:
            mandante = partida.mandante
            visitante = partida.visitante
            confrontos[(mandante, visitante)] = confrontos.get((mandante, visitante), 0) + 1

    for i in range(qtd_times):
        for j in range(i + 1, qtd_times):
            t1, t2 = times[i], times[j]
            ida = confrontos.get((t1, t2), 0)
            volta = confrontos.get((t2, t1), 0)
            assert ida == 1 and volta == 1, f"{t1} e {t2} não se enfrentaram duas vezes (ida e volta)"


@pytest.mark.funcional
@pytest.mark.parametrize("qtd_times", [4, 6, 8, 20])
def test_qtd_jogos_por_rodada_e_turnos(qtd_times):
    times = [f"Time {i+1}" for i in range(qtd_times)]
    rodadas = gerar_rodadas(times)

    num_jogos_por_rodada = qtd_times // 2
    total_rodadas = len(rodadas)
    metade = total_rodadas // 2

    for i, rodada in enumerate(rodadas, start=1):
        assert len(rodada.partidas) == num_jogos_por_rodada, (
            f"Rodada {i} deveria ter {num_jogos_por_rodada} jogos, mas tem {len(rodada.partidas)}"
        )

    confrontos_turno = set(
        (partida.mandante, partida.visitante)
        for rodada in rodadas[:metade]
        for partida in rodada.partidas
    )

    confrontos_retorno = set((v, m) for (m, v) in confrontos_turno)

    for confronto in confrontos_turno:
        assert confronto not in confrontos_retorno, (
            f"Confronto invertido encontrado no mesmo turno: {confronto}"
        )

