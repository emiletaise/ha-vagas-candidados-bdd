Feature: Encaminhar candidato para a recepção

  Scenario: Encaminhar candidato para a recepção
    Given que possuo candidatos reconhecidos
    And possuo candidatos com cadastro
    When eu encaminho o candidato para a recepção
    Then eu imprimo a mensagem de candidato sem cadastro
