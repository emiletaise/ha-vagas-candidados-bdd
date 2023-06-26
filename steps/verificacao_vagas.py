from behave import given, when, then
from candidatos import *

@given('que possuo a habilidade "{habilidade}"')
def given_possuo_habilidade(context, habilidade):
    context.habilidade = habilidade

@given('que existem vagas disponíveis')
def given_existem_vagas_disponiveis(context):
    context.vagas = {
        "vagas": [
            {"titulo": "Vaga 1", "habilidade": ["habilidade1", "habilidade2"]},
            {"titulo": "Vaga 2", "habilidade": ["habilidade3"]},
            {"titulo": "Vaga 3", "habilidade": ["habilidade1", "habilidade4"]}
        ]
    }

@when('eu verifico as vagas')
def when_verifico_vagas(context):
    context.vaga_encontrada = verificar_vagas(context.habilidade, context.configuracao, context.vagas)

@then('eu encontro uma vaga compatível')
def then_encontro_vaga_compativel(context):
    assert context.vaga_encontrada is True

@then('eu imprimo a vaga compatível')
def then_imprimo_vaga_compativel(context):
    for vaga in context.vagas["vagas"]:
        habilidades_vaga = vaga["habilidade"]
        if context.habilidade in habilidades_vaga:
            print("Vaga compatível encontrada:", vaga["titulo"])
            break
