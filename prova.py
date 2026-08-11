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

# SISTEMA DE BIBLIOTECA MENU
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

        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            print("\n--- CADASTRAR LIVRO ---")
 
            titulo = input("Título: ")
            autor = input("Autor: ")
 
            try:
                ano = int(input("Ano de publicação: "))
            except ValueError:
                print("Ano inválido.")
                continue
 
            isbn = input("Código/ISBN: ")
 
            cadastrado = cadastrar_livro(
                livros,
                titulo,
                autor,
                ano,
                isbn
            )
#Dr a função de cada opção e salvar 
            if cadastrado:
                salvar_livros(livros)
                print("Livro cadastrado com sucesso.")
            else:
                print("Já existe um livro com esse código/ISBN.")
 
        elif opcao == "2":
            print("\n--- EMPRESTAR LIVRO ---")
 
            isbn = input("Digite o código/ISBN do livro: ")
            livro = encontrar_livro_por_isbn(livros, isbn)
 
            if livro is None:
                print("Livro não encontrado.")
            elif livro["status"] == "emprestado":
                print("O livro já está emprestado.")
            else:
                livro["status"] = "emprestado"
                salvar_livros(livros)
                print("Empréstimo registrado com sucesso.")
 
        elif opcao == "3":
            print("\n--- DEVOLVER LIVRO ---")
 
            isbn = input("Digite o código/ISBN do livro: ")
            livro = encontrar_livro_por_isbn(livros, isbn)
 
            if livro is None:
                print("Livro não encontrado.")
            elif livro["status"] == "disponível":
                print("O livro já está disponível.")
            else:
                livro["status"] = "disponível"
                salvar_livros(livros)
                print("Devolução registrada com sucesso.")
 
        elif opcao == "4":
            listar_livros(livros)
 
        elif opcao == "5":
            print("\n--- BUSCAR LIVRO ---")
 
            termo = input("Digite o título ou autor: ")
           
            resultados = buscar_livros(livros, termo)
 
            if len(resultados) == 0:
                print("Nenhum livro encontrado.")
            else:
                listar_livros(resultados)
 
        elif opcao == "6":
            print("\n--- ORDENAR LIVROS ---")
            print("1 - Por título")
            print("2 - Por autor")
            print("3 - Por ano")
 
            criterio = input("Escolha uma opção: ")
 
            if criterio == "1":
                ordenado = ordenar_livros(livros, "titulo")
 
            elif criterio == "2":
                ordenado = ordenar_livros(livros, "autor")
 
            elif criterio == "3":
                ordenado = ordenar_livros(livros, "ano")
 
            else:
                ordenado = False
 
            if ordenado:
                salvar_livros(livros)
                print("Livros ordenados com sucesso.")
                listar_livros(livros)
            else:
                print("Opção de ordenação inválida.")
 
        elif opcao == "7":
            print("Programa encerrado.")
            break
 
        else:
            print("Opção inválida. Escolha uma opção de 1 a 7.")
 
 
main()

        

