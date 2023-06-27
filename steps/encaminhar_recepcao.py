from behave import given, when, then
from candidatos import *

@given('possuo candidatos reconhecidos')
def candidatos_reconhecidos(context):
    context.candidatos_reconhecidos = candidato_reconhecido_previamente()  # Implemente a função load_candidatos_reconhecidos para carregar os candidatos reconhecidos

@given('possuo candidatos com cadastro')
def candidatos_com_cadastro(context):
    context.candidatos_com_cadastro = verificar_vagas()  # Implemente a função load_candidatos_com_cadastro para carregar os candidatos com cadastro

@when('eu encaminho o candidato para a recepção')
def encaminhar_candidato_recepcao(context):
    encaminhar_recepcao(context.ambiente_de_simulacao, context.candidatos_reconhecidos, context.candidatos_com_cadastro)

@then('eu imprimo a mensagem de candidato sem cadastro')
def imprimir_mensagem_candidato_sem_cadastro(context):
    imprimir_dados_do_candidato(context.candidato)
