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

 # Busca livros pelo título/autor.
def buscar_livros(livros, termo):
    resultados = []
 
    termo = termo.lower()
 
    for livro in livros:
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
            resultados.append(livro)
 
    return resultados

 # Lista todos os livros cadastrados.
def listar_livros(livros):
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return False
 
    print("\n--- LIVROS CADASTRADOS ---")
 
    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("--------------------------")
 
    return True

# organizar os livros por título, autor e ano.
def ordenar_livros(livros, criterio):
    if criterio == "titulo":
        livros.sort(key=lambda livro: livro["titulo"].lower())
        return True
 
    elif criterio == "autor":
        livros.sort(key=lambda livro: livro["autor"].lower())
        return True
 
    elif criterio == "ano":
        livros.sort(key=lambda livro: livro["ano"])
        return True
 
    return False

#  ISBN.
def encontrar_livro_por_isbn(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro
 
    return None

# SISTEMA DE BIBLIOTECA opcoes 
def main():
    livros = carregar_livros()
 
    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1 - Cadastrar livro")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Listar livros")
        print("5 - Buscar livro")
        print("6 - Ordenar livros")
        print("7 - Sair")


