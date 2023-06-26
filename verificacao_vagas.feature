Feature: Verificando vagas disponíveis

  Scenario: Verificar vagas
    Given que possuo a habilidade "habilidade_do_candidato"
    And que existem vagas disponíveis
    When eu verifico as vagas
    Then eu encontro uma vaga compatível
    And eu imprimo a vaga compatível

