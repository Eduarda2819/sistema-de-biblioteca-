import csv

ARQUIVO = "livros.csv"

#livros do arquivo CSV para a lista
def carregar_livros():
    livros = []

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for livro in leitor:
                livro["ano"] = int(livro["ano"])
                livros.append(livro)

    except FileNotFoundError:
        pass

    return livros

# Salva todos os livros da lista no arquivo CSV.
def salvar_livros(livros):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["titulo", "autor", "ano", "isbn", "status"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
 
        escritor.writeheader()
        escritor.writerows(livros)
  
    return True

# Cadastro do livro 
def cadastrar_livro(livros, titulo, autor, ano, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return False
 
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }
 
    livros.append(novo_livro)
    return True
 
 


