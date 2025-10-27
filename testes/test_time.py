import pytest
from src.time import Time

nome_times = ["Corinthians", "Framengo", "Boladefogo"]

resultados = [
    (2, 0, 3, 1, 0, 0, 2),   # vitória
    (1, 1, 1, 0, 1, 0, 0),   # empate
    (0, 3, 0, 0, 0, 1, -3),  # derrota
]

@pytest.mark.funcional
@pytest.mark.parametrize("nome_esperado", nome_times)
def test_construtor(nome_esperado):
    time = Time(nome_esperado)
    assert time.nome == nome_esperado
    assert time.pontos == 0
    assert time.vitorias == 0
    assert time.empates == 0
    assert time.derrotas == 0
    assert time.gols_marcados == 0
    assert time.gols_sofridos == 0
    assert time.saldo_gols == 0

@pytest.mark.funcional
@pytest.mark.parametrize("nome_esperado", nome_times)
def test_vitoria(nome_esperado):
    time = Time(nome_esperado)
    time.adicionar_vitoria(gols_pro=3, gols_contra=1)
    assert time.pontos == 3
    assert time.vitorias == 1
    assert time.empates == 0
    assert time.derrotas == 0
    assert time.gols_marcados == 3
    assert time.gols_sofridos == 1
    assert time.saldo_gols == 2

@pytest.mark.funcional
@pytest.mark.parametrize("nome_esperado", nome_times)
def test_empate(nome_esperado):
    time = Time(nome_esperado)
    time.adicionar_empate(gols_pro=2, gols_contra=2)
    assert time.pontos == 1
    assert time.vitorias == 0
    assert time.empates == 1
    assert time.derrotas == 0
    assert time.gols_marcados == 2
    assert time.gols_sofridos == 2
    assert time.saldo_gols == 0

@pytest.mark.funcional
@pytest.mark.parametrize("nome_esperado", nome_times)
def test_derrota(nome_esperado):
    time = Time(nome_esperado)
    time.adicionar_derrota(gols_pro=0, gols_contra=4)
    assert time.pontos == 0
    assert time.vitorias == 0
    assert time.empates == 0
    assert time.derrotas == 1
    assert time.gols_marcados == 0
    assert time.gols_sofridos == 4
    assert time.saldo_gols == -4


@pytest.mark.funcional
@pytest.mark.parametrize("nome_esperado", nome_times)
@pytest.mark.parametrize(
    "gols_pro, gols_contra, pontos_esperados, vitorias, empates, derrotas, saldo",
    resultados
)
def test_registrar_resultado(nome_esperado, gols_pro, gols_contra, pontos_esperados, vitorias, empates, derrotas, saldo):
    time = Time(nome_esperado)
    time.registrar_resultado(gols_pro, gols_contra)
    assert time.pontos == pontos_esperados
    assert time.vitorias == vitorias
    assert time.empates == empates
    assert time.derrotas == derrotas
    assert time.gols_marcados == gols_pro
    assert time.gols_sofridos == gols_contra
    assert time.saldo_gols == saldo

@pytest.mark.funcional
@pytest.mark.parametrize("nome_esperado", nome_times)
def test_repr_contem_informacoes_relevantes(nome_esperado):
    time = Time(nome_esperado)
    time.registrar_resultado(2, 1)
    texto = repr(time)
    assert time.nome in texto
    assert f"{time.pontos} pts" in texto
    assert f"{time.vitorias}V" in texto
    assert "SG" in texto

