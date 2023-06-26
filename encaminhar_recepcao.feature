Feature: Encaminhar visitante para a recepção

  Scenario: Encaminhar candidato para a recepção
    Given que possuo um candidato sem cadastro
    When eu encaminho o candidato para a recepção
    Then o candidato é encaminhado corretamente
    And eu imprimo a mensagem de candidato sem cadastro

