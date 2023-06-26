from behave import given, when, then
from candidatos import *

@given("o ambiente de reconhecimento seja preparado com sucesso")
def given_ambiente_preparado_com_sucesso(context):
    preparado, context.configuracao = ler_configuracao()
    context.candidatos_reconhecidos = {}

    assert preparado

@when("a foto {foto} de visitantes for capturada")
def when_foto_de_visitantes_capturada(context, foto):
    context.visitantes = simular_visitas(foto)

    assert context.visitantes is not None

@then('pelo menos, um(a) visitante deve ser reconhecido(a)')
def then_um_candidato_reconhecido(context):
    candidatos_reconhecidos, context.candidatos = reconhecer_candidatos(context.visitantes, context.configuracao, context.candidatos_reconhecidos)
    assert len(candidatos_reconhecidos) > 0, "Nenhum visitante foi reconhecido."

@then("nenhum(a) candidato deve ser reconhecido(a)")
def then_nenhum_candidato_reconhecido(context):
    candidatos_reconhecidos, _ = reconhecer_candidatos(context.configuracao, context.visitantes)

    assert not candidatos_reconhecidos

@then("{total_de_reconhecimentos} candidatos devem ser reconhecidos")
def then_total_de_candidatos_reconhecidos(context, total_de_reconhecimentos):
    _, context.candidatos = reconhecer_candidatos(context.configuracao, context.visitantes)

    assert len(context.candidatos) == int(total_de_reconhecimentos)