from behave import given, when, then
from candidatos import * 

@given('existem candidatos aptos')
def existe_candidatos_apto(context):
    context.candidatos_apto = candidato_reconhecido_previamente()

@when('agendo a entrevista')
def agendo_entrevista(context):
    entrevista_generator = agendar_entrevista(context.ambiente_de_simulacao, context.candidatos_apto)
    context.entrevista_iterator = iter(entrevista_generator)

@then('a entrevista é agendada para uma vaga compatível')
def entrevista_agendada(context):
    try:
        next(context.entrevista_iterator)
    except StopIteration:
        pass
