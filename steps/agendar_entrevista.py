from behave import given, when, then
from candidatos import *

@given('eu possuo um candidato com habilidade "{habilidade}"')
def given_possuo_candidato_com_habilidade(context, habilidade):
    context.candidato = {
        "habilidade": habilidade,
        "cadastro": True
    }

@when('eu agendo a entrevista')
def when_agendo_entrevista(context):
    agendar_entrevista(context.candidato, context.vagas)

@then('a entrevista deve ser agendada para uma vaga compatível')
def then_entrevista_agendada(context):
    habilidade_do_candidato = context.habilidade_do_candidato
    configuracao = ler_configuracao()
    vagas = ler_vagas()

    if verificar_vagas(habilidade_do_candidato, configuracao, vagas):
        candidato = {"habilidade": habilidade_do_candidato}
        agendar_entrevista(candidato, vagas)
    else:
        raise AssertionError("Nenhuma vaga compatível encontrada para a habilidade do candidato.")

