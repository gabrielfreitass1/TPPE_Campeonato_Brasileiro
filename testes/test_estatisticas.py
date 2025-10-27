from src.time import Time
from src.classificacao import Classificacao
from src.partida import Partida


def test_estatisticas_partida_unica_atualiza_gols_saldo_e_pontos():
    
    a = Time("A")
    b = Time("B")

    Partida(a, b, gols_mandante=3, gols_visitante=1).jogar()

    assert a.vitorias == 1
    assert a.empates == 0
    assert a.derrotas == 0
    assert a.pontos == 3
    assert a.gols_marcados == 3
    assert a.gols_sofridos == 1
    assert a.saldo_gols == 2

    assert b.vitorias == 0
    assert b.empates == 0
    assert b.derrotas == 1
    assert b.pontos == 0
    assert b.gols_marcados == 1
    assert b.gols_sofridos == 3
    assert b.saldo_gols == -2


def test_acumulo_estatisticas_em_varias_partidas():
    
    a = Time("A")
    b = Time("B")
    c = Time("C")
    d = Time("D")

    Partida(a, b, 2, 0).jogar()
    Partida(a, c, 1, 1).jogar()
    Partida(a, d, 0, 1).jogar()

    assert a.vitorias == 1
    assert a.empates == 1
    assert a.derrotas == 1
    assert a.pontos == 4               
    assert a.gols_marcados == 3        
    assert a.gols_sofridos == 2        
    assert a.saldo_gols == 1           


def test_desempate_primeiro_por_vitorias():
    
    a = Time("Time A")
    b = Time("Time B")

    for _ in range(3):
        a.adicionar_vitoria(0, 0)
    for _ in range(3):
        a.adicionar_derrota(0, 0)
    for _ in range(2):
        b.adicionar_vitoria(0, 0)
    for _ in range(3):
        b.adicionar_empate(0, 0)
    b.adicionar_derrota(0, 0)

    tabela = Classificacao([a, b]).gerar_tabela()
    assert tabela[0].nome == "Time A"
    assert tabela[1].nome == "Time B"


def test_desempate_segundo_por_saldo_quando_vitorias_iguais():
   
    a = Time("Time A")
    b = Time("Time B")

    a.adicionar_vitoria(1, 0)
    a.adicionar_vitoria(2, 0)
    a.adicionar_empate(0, 0)

    b.adicionar_vitoria(3, 2)
    b.adicionar_vitoria(1, 0)
    b.adicionar_empate(0, 0)

    assert a.pontos == b.pontos == 7
    assert a.vitorias == b.vitorias == 2

    tabela = Classificacao([a, b]).gerar_tabela()
    assert tabela[0].nome == "Time A"   
    assert tabela[1].nome == "Time B"


def test_desempate_terceiro_por_gols_marcados_quando_saldo_igual():
    
    a = Time("Time A")
    b = Time("Time B")

    a.adicionar_vitoria(2, 1)
    a.adicionar_vitoria(1, 0)
    a.adicionar_empate(0, 0)

    b.adicionar_vitoria(3, 2)
    b.adicionar_vitoria(2, 1)
    b.adicionar_empate(0, 0)

    assert a.pontos == b.pontos == 7
    assert a.vitorias == b.vitorias == 2
    assert a.saldo_gols == b.saldo_gols == 2
    assert b.gols_marcados > a.gols_marcados

    tabela = Classificacao([a, b]).gerar_tabela()
    assert tabela[0].nome == "Time B"
    assert tabela[1].nome == "Time A"


def test_empate_espelhado_mantem_consistencia_nos_dois_lados():
   
    m = Time("Mandante")
    v = Time("Visitante")

    Partida(m, v, 4, 4).jogar()

    assert m.empates == 1
    assert m.pontos == 1
    assert m.gols_marcados == 4
    assert m.gols_sofridos == 4
    assert m.saldo_gols == 0

    assert v.empates == 1
    assert v.pontos == 1
    assert v.gols_marcados == 4
    assert v.gols_sofridos == 4
    assert v.saldo_gols == 0
