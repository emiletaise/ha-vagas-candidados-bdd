Feature: Agendar Entrevista

  Scenario: Agendar entrevista
    Given existem candidatos aptos
    When agendo a entrevista
    Then a entrevista é agendada para uma vaga compatível
