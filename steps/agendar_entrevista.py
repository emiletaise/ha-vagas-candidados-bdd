from behave import given, when, then
from candidatos import *

@given('existem candidatos aptos')
def existem_candidatos_aptos(context):
    context.candidatos_aptos = candidato_reconhecido_previamente  # Implemente a função para carregar os candidatos aptos

@when('agendo a entrevista')
def agendo_entrevista(context):
    entrevista_agendada = agendar_entrevista(context.candidatos_aptos())  # Implemente a função para agendar a entrevista
    context.entrevista_agendada = entrevista_agendada

@then('a entrevista é agendada para uma vaga compatível')
def entrevista_agendada_para_vaga_compativel(context):
    assert context.entrevista_agendada is not None, "A entrevista não foi agendada"
    assert context.entrevista_agendada.vaga.compativel, "A entrevista foi agendada para uma vaga incompatível"
