import face_recognition as reconhecedor
import colored
import random
import json

ARQUIVO_DE_CONFIGURACAO = "../candidatos/configuracao.json"

# Função para ler as configurações do arquivo JSON
def ler_configuracao():
    
    try:
        with open(ARQUIVO_DE_CONFIGURACAO, "r") as arquivo:
            configuracao = json.load(arquivo)
            if configuracao:
                print("Arquivo de configuração carregado")
                return configuracao
    except Exception as e:
        print(f"Erro ao ler configuração: {str(e)}")
    return None

def simular_visitas(foto):
    print(f"Foto de visitantes: {foto}")

    visitantes = {
        "foto": foto,
        "candidatos": []
    }
    return visitantes

def candidato_reconhecido_previamente(candidato, candidatos_reconhecidos):
    reconhecido_previamente = False
    for reconhecido in candidatos_reconhecidos.values():
        if candidato["codigo"] == reconhecido["codigo"]:
            reconhecido_previamente = True
            break
    return reconhecido_previamente

def reconhecer_candidatos(visitantes, configuracao, candidatos_reconhecidos):
    print("Realizando reconhecimento de candidatos...")
    foto_visitantes = reconhecedor.load_image_file(visitantes["foto"])
    caracteristicas_dos_visitantes = reconhecedor.face_encodings(foto_visitantes)

    candidatos = []
    for candidato in configuracao["candidatos"]:
        if not candidato_reconhecido_previamente(candidato, candidatos_reconhecidos):
            fotos = candidato["fotos"]
            total_de_reconhecimentos = 0

            for foto in fotos:
                foto = reconhecedor.load_image_file(foto)
                caracteristicas = reconhecedor.face_encodings(foto)[0]

                reconhecimentos = reconhecedor.compare_faces(
                    caracteristicas_dos_visitantes, caracteristicas)
                if True in reconhecimentos:
                    total_de_reconhecimentos += 1

            if total_de_reconhecimentos / len(fotos) >= 0.6:
                candidatos.append(candidato)
        else:
            print("Candidato reconhecido previamente")
    return (len(candidatos) > 0), candidatos, candidatos_reconhecidos

def imprimir_dados_do_candidato(candidato):
    print(colored.fg('black'), colored.bg(
        'yellow'), f"candidato reconhecido:", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"nome: {candidato['nome']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"idade: {candidato['idade']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"tem cadastro: {candidato['cadastro']}", colored.attr('reset'))

def verificacao_vagas():
    vaga = random.choice([True, False])
    print("Disponibilidade de vagas: ", vaga) 
    return vaga

def agendar_entrevista(vaga):
    disponibilidade = verificacao_vagas()
    if disponibilidade == True:
        print(f"Entrevista agendada")
    else: 
        print(f"Não há disponibilidade de vagas")

    return disponibilidade

def reconhecer_visitantes(ambiente_de_simulacao, configuracao, candidatos_reconhecidos):
    while True:
        print(f"Tentando reconhecer um candidato entre visitantes em {ambiente_de_simulacao.now}")

        visitantes = simular_visitas()
        ocorreram_reconhecimentos, candidatos = reconhecer_candidatos(visitantes, configuracao, candidatos_reconhecidos)

        if ocorreram_reconhecimentos:
            for candidato in candidatos:
                imprimir_dados_do_candidato(candidato)
                if candidato['cadastro'] == True:
                   agendar_entrevista()

        yield ambiente_de_simulacao.timeout(40)  # Tempo de detecção de candidatos
