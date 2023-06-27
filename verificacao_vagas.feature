Feature: Verificar Vagas

  Scenario: Verificar vagas disponíveis
    Given existem candidatos aptos
    When verifico as vagas
    Then encontro vagas compatíveis
    And imprimo as vagas compatíveis
