from behave import given, when, then
from candidatos import *

@given('uma vaga de emprego disponível')
def given_vaga_disponivel(context):
    context.vaga = True

@when('tento agendar uma entrevista')
def when_tento_agendar_entrevista(context):
    context.resultado_agendamento = agendar_entrevista(context.vaga)

@then('a entrevista deve ser agendada')
def then_entrevista_deve_ser_agendada(context):
    assert context.resultado_agendamento is True

@given('uma vaga de emprego indisponível')
def given_vaga_indisponivel(context):
    context.vaga = False

@then('a entrevista não deve ser agendada')
def then_entrevista_nao_deve_ser_agendada(context):
    assert context.resultado_agendamento is False
