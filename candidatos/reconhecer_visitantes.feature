Feature: reconhecimento de visitante

    Scenario: um visitante deve ser reconhecido a partir da entrada na agencia de vagas de emprego
        Given o ambiente de reconhecimento seja preparado com sucesso
        When a foto faces/Robin1.jpg de visitantes for capturada
        Then pelo menos, um(a) visitante deve ser reconhecido(a)

    Scenario: nao deve reconhecer candidatos quando eles nao estao entre os visitantes
        Given o ambiente de reconhecimento seja preparado com sucesso
        When a foto faces\personagens3.jpeg de visitantes for capturada
        Then nenhum(a) candidatos deve ser reconhecido(a)

    Scenario Outline: reconhecer candidatos de varias fotos diferentes
        Given o ambiente de reconhecimento seja preparado com sucesso
        When a foto <foto_capturada> de visitantes for capturada
        Then <total_de_reconhecimentos> candidatos devem ser reconhecidos

