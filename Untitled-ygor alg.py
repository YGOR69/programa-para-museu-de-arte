
import datetime

class Artista:
    def __init__(self, nome, data_nascimento, local_nascimento, biografia, estilos):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.local_nascimento = local_nascimento
        self.biografia = biografia
        self.estilos = estilos  # lista de estilos associados ao artista

class EstiloArtistico:
    def __init__(self, denominacao, periodo, caracteristicas, escola):
        self.denominacao = denominacao
        self.periodo = periodo
        self.caracteristicas = caracteristicas
        self.escola = escola

class ObraDeArte:
    def __init__(self, titulo, data_criacao, tema, estilo, descricao, tecnica, autor, localizacao):
        self.titulo = titulo
        self.data_criacao = data_criacao
        self.tema = tema
        self.estilo = estilo
        self.descricao = descricao
        self.tecnica = tecnica
        self.autor = autor
        self.localizacao = localizacao
        self.documentos_relacionados = []  # lista de documentos relacionados
        self.pessoa_retratada = None  # objeto Pessoa se a obra retrata alguém

    def adicionar_documento(self, documento):
        self.documentos_relacionados.append(documento)

    def adicionar_pessoa_retratada(self, pessoa):
        self.pessoa_retratada = pessoa

class Pessoa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class EmprestimoObra:
    def __init__(self, obra, periodo_emprestimo, nome_evento, responsavel, tema):
        self.obra = obra
        self.periodo_emprestimo = periodo_emprestimo
        self.nome_evento = nome_evento
        self.responsavel = responsavel
        self.tema = tema

class VisitaGuiada:
    def __init__(self, tema, descricao, obras):
        self.tema = tema
        self.descricao = descricao
        self.obras = obras  

        def ordenar_obras_por_data(obras):
    return sorted(obras, key=lambda x: x.data_criacao)

def salvar_obras_em_arquivo(obras, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as file:
            for obra in obras:
                file.write(f"{obra.titulo};{obra.data_criacao};{obra.autor}\n")
    except IOError:
        print("Erro ao salvar arquivo.")

def carregar_obras_de_arquivo(nome_arquivo):
    obras = []
    try:
        with open(nome_arquivo, 'r') as file:
            for line in file:
                dados = line.strip().split(';')
                titulo, data_criacao, autor = dados
                obra = ObraDeArte(titulo, datetime.datetime.strptime(data_criacao, '%Y-%m-%d').date(), '', '', '', '', autor, '')
                obras.append(obra)
    except IOError:
        print("Erro ao carregar arquivo.")
    return obras

# Exemplo de uso
if __name__ == "__main__":
    # Criar objetos
    obras = [
        ObraDeArte("Mona Lisa", datetime.date(1503, 1, 1), "Retrato", "Renascimento", "Descrição da obra", "Óleo sobre tela", "Leonardo da Vinci", "Sala 1"),
        ObraDeArte("Noite Estrelada", datetime.date(1889, 1, 1), "Paisagem Noturna", "Pós-Impressionismo", "Descrição da obra", "Óleo sobre tela", "Vincent van Gogh", "Sala 2")
    ]

    # Ordenar obras por data de criação
    obras_ordenadas = ordenar_obras_por_data(obras)

    # Salvar obras em arquivo
    salvar_obras_em_arquivo(obras_ordenadas, "obras.txt")

    # Carregar obras de arquivo
    obras_carregadas = carregar_obras_de_arquivo("obras.txt")
    for obra in obras_carregadas:
        print(f"{obra.titulo} - {obra.data_criacao} - {obra.autor}")