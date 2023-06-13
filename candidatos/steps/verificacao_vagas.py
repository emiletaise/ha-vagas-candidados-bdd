from behave import given, when, then
from candidatos import *

@given('uma vaga de emprego')
def given_vaga_de_emprego(context):
    context.vaga = None

@when('verifico a disponibilidade de vagas')
def when_verifico_disponibilidade_vagas(context):
    context.vaga = verificacao_vagas()

@then('devo obter o resultado da verificação')
def then_obter_resultado_verificacao(context):
    assert context.vaga is not None
