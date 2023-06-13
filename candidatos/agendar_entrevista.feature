Feature: Agendamento de Entrevista

  Scenario: Agendar entrevista com vaga disponível
    Given uma vaga de emprego disponível
    When tento agendar uma entrevista
    Then a entrevista deve ser agendada

  Scenario: Agendar entrevista sem vaga disponível
    Given uma vaga de emprego indisponível
    When tento agendar uma entrevista
    Then a entrevista não deve ser agendada

