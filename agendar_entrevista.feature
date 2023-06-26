Feature: Agendar entrevista

  Scenario: Agendar entrevista
    Given que existem vagas disponíveis
    And eu possuo um candidato com habilidade "habilidade_do_candidato"
    When eu agendo a entrevista
    Then a entrevista deve ser agendada para uma vaga compatível
