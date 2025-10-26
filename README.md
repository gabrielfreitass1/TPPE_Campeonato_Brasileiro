# TPPE_Campeonato_Brasileiro
Trabalho da Disciplina de Técnicas de Programação para Plataformas Emergentes do professor Andre Lanna da UNB

## Equipe

Gabriel Freitas Balbino - 180075462
Rodrigo Mattos de Figueiredo Ayres Bezerra - 180108875

## Objetivo do trabalho
O objetivo deste trabalho é desenvolver uma aplicação em python que simule o funcionamento do Campeonato Brasileiro Série A de 2025, utilizando conceitos os seguintes conceitos:
 - Test-Driven Development (TDD)
 - Code Smells
 - Refactoring
 - Design by Contracts (DbC)

A aplicação deve ser capaz de:
1. Realizar os sorteios de jogos de cada rodada;
2. Garantir que não existam dois jogos iguais ao longo de todas as rodadas (por "jogos iguais" entenda jogos com os mesmos times como mandantes e visitantes);
3. Calcular a pontuação dos times e a classificação a cada rodada, conforme os critérios de pontuação apresentados no enunciado (vitória = 3 pontos, empate = 1 ponto, derrota = 0 pontos);
4. Calcular os números de vitórias, gols marcados, gols sofridos e saldos de gols com base nos resultados dos jogos de cada rodada;
5. Aplicar o critério de desempate pelo número de vitórias.


Nosso sistema utiliza os testes unitários desenvolvidos com o framework pytest.
## Estrutura de Arquivos
```
TPPE_Campeonato_Brasileiro/
│
├── src/
│   ├── __init__.py
│   ├── main.py                    # Ponto de entrada (ex: simula o campeonato completo)
│   ├── time.py                    # Classe Time (nome, gols, pontos, vitórias etc.)
│   ├── partida.py                 # Classe Partida (mandante, visitante, placar etc.)
│   ├── rodada.py                  # Lógica para gerar rodadas (sorteios de jogos)
│   ├── classificacao.py           # Calcula a tabela de classificação
│   └── utils.py                   # Funções auxiliares (ex: critério de desempate)
│
├── tests/
│   ├── __init__.py
│   ├── test_time.py               # Testes unitários da classe Time
│   ├── test_partida.py            # Testes da lógica de partidas
│   ├── test_rodada.py             # Testes do sorteio e geração de rodadas
│   ├── test_classificacao.py      # Testes do cálculo da tabela e desempates
│   └── test_alltests.py           # Suíte "AllTests" que executa todos os testes
│
├── requirements.txt               # Dependências
└── README.md                      # Instruções do trabalho

```
## Instruções de Uso
1. **Requisitos de Ambiente**:
   - Python 3.8+
   - Pytest 8.4.2+

2. **Instalação de Dependências**:
   ``` 
    pip install -r requirements.txt
   ```

3. **Execução dos Tetes**:
    ``` 
    pytest -v
    ```