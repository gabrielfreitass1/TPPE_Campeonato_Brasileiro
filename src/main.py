from src.time import Time
from src.classificacao import Classificacao
from src.rodada import gerar_rodadas

def exibir_classificacao(times):
    classificacao = Classificacao(times)
    tabela = classificacao.gerar_tabela()
    print("\n=== Classificação Atual ===")
    print(f"{'Time':15} {'Pts':>3} {'Vit':>3} {'GM':>3} {'GS':>3} {'SG':>3}")
    for t in tabela:
        print(f"{t.nome:15} {t.pontos:3} {t.vitorias:3} {t.gols_marcados:3} {t.gols_sofridos:3} {t.saldo_gols:3}")

def main():
    times = [
        Time("Cruzeiro"),
        Time("São Paulo"),
        Time("Santos"),
        Time("Internacional")
    ]

    rodadas = gerar_rodadas(times, seed=2025)

    for rodada in rodadas:
        rodada.jogar()
        exibir_classificacao(times)

    print("\n🏆 === Fim do Campeonato! ===")
    print("\n=== Classificação Final ===")
    exibir_classificacao(times)

    campeao = max(times, key=lambda t: (t.pontos, t.vitorias, t.saldo_gols, t.gols_marcados))
    print(f"\nCampeão: {campeao.nome}")

if __name__ == "__main__":
    main()
