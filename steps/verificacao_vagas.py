from behave import given, when, then
from candidatos import *


@given('possue candidatos aptos')
def candidatos_apto(context):
    context.candidatos_apto = {}

@when('verifico as vagas')
def verifico_vagas(context):
    vagas_generator = verificar_vagas(context.ambiente_de_simulacao, context.vagas,
                                     context.candidatos_com_cadastro, context.candidatos_apto)
    context.vagas_iterator = iter(vagas_generator)

@then('encontro vagas compatíveis')
def encontro_vagas_compativeis(context):
    try:
        next(context.vagas_iterator)
    except StopIteration:
        pass


@then('imprimo as vagas compatíveis')
def imprimo_vagas_compativeis(context):
    try:
        next(context.vagas_iterator)
    except StopIteration:
        pass
