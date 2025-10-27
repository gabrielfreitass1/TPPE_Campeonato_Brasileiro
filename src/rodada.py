def gerar_rodadas(times):
    # Se número ímpar de times, adiciona um time "Folga"
    if len(times) % 2 != 0:
        times.append("Folga")

    num_times = len(times)
    num_rodadas = num_times - 1
    metade = num_times // 2

    rodadas = []
    for r in range(num_rodadas):
        rodada = []
        for i in range(metade):
            mandante = times[i]
            visitante = times[num_times - 1 - i]
            if mandante != "Folga" and visitante != "Folga":
                rodada.append((mandante, visitante))
        rodadas.append(rodada)

        times = [times[0]] + [times[-1]] + times[1:-1]

    rodadas_volta = [[(v, m) for (m, v) in rodada] for rodada in rodadas]

    return rodadas + rodadas_volta
