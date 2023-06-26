from behave import given, when, then
from candidatos import *

@given('que possuo um candidato sem cadastro')
def given_possuo_candidato_sem_cadastro(context):
    context.candidato = {
        "nome": "Candidato Sem Cadastro",
        "cadastro": False
    }

@when('eu encaminho o candidato para a recepção')
def when_encaminho_candidato_recepcao(context):
    encaminhar_recepcao(context.candidato)

@then('o candidato é encaminhado corretamente')
def then_candidato_encaminhado_corretamente(context):
    assert context.candidato["nome"] == "Candidato Sem Cadastro"

@then('eu imprimo a mensagem de candidato sem cadastro')
def then_imprimo_mensagem_candidato_sem_cadastro(context):
    assert "Candidato sem cadastro!" in context.printed_messages


