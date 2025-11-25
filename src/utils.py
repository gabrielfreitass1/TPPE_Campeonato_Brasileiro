def determina_resultado(time, gols_pro, gols_contra):
    if gols_pro > gols_contra:
        return time.adicionar_vitoria(gols_pro, gols_contra)

    if gols_pro == gols_contra:
        return time.adicionar_empate(gols_pro, gols_contra)

    return time.adicionar_derrota(gols_pro, gols_contra)