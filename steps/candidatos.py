import face_recognition as reconhecedor
import colored
import simpy
import json

ARQUIVO_DE_CONFIGURACAO = "../ha-vagas-candidatos-bdd/configuracao.json"
ARQUIVO_DE_VAGAS = "../ha-vagas-candidatos-bdd/vagas.json"

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

# Função para ler as vagas do arquivo JSON
def ler_vagas():
    try:
        with open(ARQUIVO_DE_VAGAS, "r") as arquivo:
            vagas = json.load(arquivo)
            if vagas:
                print("Arquivo de vagas carregado")
                return vagas
    except Exception as e:
        print(f"Erro ao ler vagas: {str(e)}")
    return None

def simular_visitas(foto):
    print(f"Foto de visitantes: {foto}")

    visitantes = {
        "foto": foto,
        "pacientes": None
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

    for candidato in candidatos:
        if candidato['cadastro'] == False:
            encaminhar_recepcao(candidato)

    return (len(candidatos) > 0), candidatos

def imprimir_dados_do_candidato(paciente):
    print(colored.fg('black'), colored.bg(
        'yellow'), f"candidato reconhecido:", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"nome: {paciente['nome']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"idade: {paciente['idade']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"tem cadastro: {paciente['cadastro']}", colored.attr('reset'))
    

def verificar_vagas(habilidade, configuracao, vagas):
    for vaga in vagas["vagas"]:
        habilidades_vaga = vaga['habilidade']
        if habilidade in habilidades_vaga:
            print("Vaga compatível encontrada:", vaga["titulo"])
            return True
    return False

def agendar_entrevista(candidato, vagas):
    habilidade_candidato = candidato['habilidade']
    vagas_compativeis = []

    for vaga in vagas["vagas"]:
        habilidades_vaga = vaga['habilidade']
        if habilidade_candidato in habilidades_vaga:
            vagas_compativeis.append(vaga)

    if len(vagas_compativeis) == 0:
        print("Não há disponibilidade de vagas para a habilidade do candidato.")
    else:
        vaga_escolhida = vagas_compativeis[0]
        print("Entrevista agendada para a vaga:", vaga_escolhida["titulo"])

def encaminhar_recepcao(candidato):

    print("Encaminhando candidato para a recepção:", candidato["nome"])
    if not candidato["cadastro"]:
        print("Candidato sem cadastro!")
    
def reconhecer_visitantes(ambiente_de_simulacao, configuracao, vagas, candidatos_reconhecidos):
    while True:
        print(f"Tentando reconhecer um candidato entre visitantes em {ambiente_de_simulacao.now}")

        visitantes = simular_visitas()
        ocorreram_reconhecimentos, candidatos = reconhecer_candidatos(visitantes, configuracao, candidatos_reconhecidos)

        if ocorreram_reconhecimentos:
            for candidato in candidatos:
                imprimir_dados_do_candidato(candidato)
                if candidato['cadastro'] == True:
                    agendar_entrevista(candidato, vagas)
        # Tempo de detecção de candidatos
        yield ambiente_de_simulacao.timeout(40) 