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


