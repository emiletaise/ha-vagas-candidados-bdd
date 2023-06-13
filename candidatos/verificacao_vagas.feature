Feature: Verificação de Vagas

  Scenario: Verificar disponibilidade de vagas
    Given uma vaga de emprego
    When verifico a disponibilidade de vagas
    Then devo obter o resultado da verificação
