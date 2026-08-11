Sistema de biblioteca 
Eu desenvolvi este projeto em Python com o objetivo de criar um sistema simples para organizar os livros de uma biblioteca.
No programa, é possível cadastrar livros, registrar empréstimos e devoluções, visualizar os livros cadastrados, pesquisar por título ou autor e organizar a lista por título, autor ou ano de publicação.
Para não perder os livros quando o programa é fechado, utilizei o arquivo livros.csv. Quando o programa é iniciado, ele lê esse arquivo e coloca os livros novamente na lista.
Cada livro possui cinco informações:
Título
Autor
Ano de publicação
ISBN
Status
O status começa como "disponível" quando o livro é cadastrado e pode mudar para "emprestado" ou voltar para "disponível"
Na opção de cadastro, o programa pede o título, autor, ano de publicação e ISBN.
Depois dessas informações, o livro é colocado na lista com o status "disponível".
Também fiz uma verificação para não permitir dois livros com o mesmo ISBN. Se o código já estiver cadastrado, o programa informa:
Já existe um livro com esse código/ISBN.
Também existe uma verificação para o ano de publicação. Caso seja digitado algo que não seja um número, o programa informa que o ano é inválido.

Emprestar livro

Para emprestar um livro, o usuário informa o ISBN.
O programa procura esse ISBN na lista. Se não encontrar, informa que o livro não foi encontrado.
Se o livro estiver disponível, seu status passa para "emprestado" e as informações são salvas novamente no arquivo livros.csv.
Caso ele já esteja emprestado, o programa avisa que o empréstimo não pode ser feito novamente.

Devolver livro
A devolução também é feita pelo ISBN.
Se o livro estiver emprestado, seu status volta para "disponível" e a alteração é salva no arquivo.
Se o livro não existir ou já estiver disponível, o programa informa a situação ao usuário.

Listar livros
A opção de listar mostra todos os livros cadastrados.
Para cada livro, são mostrados:
Título
Autor
Ano
ISBN
Status
Se ainda não houver nenhum livro cadastrado, o programa informa que não há livros cadastrados.

Buscar livro
A busca pode ser feita pelo título ou pelo autor.
Eu fiz a busca de uma forma que não precisa escrever o nome exatamente igual. Por exemplo, se existir um livro com o autor "Machado de Assis", pesquisar apenas "machado" já pode encontrar o livro.
Também não importa se o usuário digitar letras maiúsculas ou minúsculas.
Os resultados encontrados são mostrados usando a mesma função utilizada para listar os livros.

Ordenar livros
A opção de ordenação permite escolher entre:
Ordenar por título;
Ordenar por autor;
Ordenar por ano
Quando a ordenação é feita, a lista é reorganizada e salva novamente no livros.csv.
No programa, os livros ficam em uma lista de dicionários.
Cada dicionário representa um livro. Por exemplo:

{
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899,
    "isbn": "123456",
    "status": "disponível"
}

A lista pode ter vários desses dicionários, um para cada livro cadastrado.

Salvamento dos livros
Para salvar os dados, utilizei o arquivo livros.csv.
Quando o programa começa, a função carregar_livros() tenta abrir o arquivo e recuperar os livros que já foram cadastrados.
Quando faço uma alteração, utilizo a função salvar_livros() para atualizar o arquivo.
Isso acontece, por exemplo, quando:
Um livro é cadastrado
Um livro é emprestado
Um livro é devolvido
A lista de livros é ordenada.
Caso o arquivo ainda não exista, o programa consegue iniciar normalmente sem apresentar erro. Nesse caso, a lista começa vazia.

Organização do código

Dividi o programa em várias funções para não deixar toda a lógica dentro do menu.
As principais funções são:
carregar_livros() — carrega os livros que estão no arquivo.
salvar_livros(livros) — salva a lista de livros no arquivo.
cadastrar_livro — verifica o ISBN e cadastra um novo livro.
buscar_livros(livros, termo) — procura livros pelo título ou autor.
listar_livros(livros) — mostra os livros cadastrados.
ordenar_livros(livros, criterio) — organiza os livros pelo critério escolhido.
encontrar_livro_por_isbn(livros, isbn) — encontra um livro específico pelo ISBN.
main() — inicia o sistema e controla o menu.
Requisitos técnicos utilizados

Durante o desenvolvimento, apliquei os requisitos pedidos na atividade:
Menu principal com if/elif/else: usado na função main() para controlar as sete opções do sistema.
while: utilizado para manter o menu funcionando até o usuário escolher a opção de sair.
Funções próprias: criei várias funções com diferentes responsabilidades, como cadastro, busca, listagem, ordenação e carregamento dos dados.
Lista de dicionários: os livros ficam armazenados em uma lista, com um dicionário para cada livro.
Persistência em arquivo: utilizei o livros.csv para salvar e recuperar os livros.
Leitura e escrita de arquivo: utilizei o módulo csv do próprio Python para trabalhar com o arquivo.
Comentários: coloquei comentários nas principais partes do código para identificar e explicar suas funções.
Estrutura do repositório
nome-do-projeto/
main.py
livros.csv
README.md

O main.py contém o programa, o livros.csv guarda os dados dos livros e o README.md explica o projeto e como utilizá-lo.
Git e GitHub
Durante o desenvolvimento, o projeto foi versionado com Git e enviado para o GitHub.
A ideia dos commits é registrar as etapas do desenvolvimento, mostrando a evolução do projeto em vez de fazer todas as alterações em um único commit.
As mensagens dos commits descrevem o que foi desenvolvido em cada etapa, como cadastro de livros, busca, ordenação e persistência dos dados.
om este projeto, coloquei em prática os conteúdos de Python trabalhados na atividade, principalmente listas, dicionários, funções, if/elif/else, while, leitura e escrita de arquivos e organização do código.
Além de fazer as funções principais de uma biblioteca, procurei colocar algumas verificações para evitar situações incorretas, como cadastrar dois livros com o mesmo ISBN ou emprestar um livro que já está emprestado, apesar das dificuldades eu consegui terminar ele, fiz o código em casa durante 4 dias, perdi a senha do GitHub mas consegui entrar na escola, tive ajuda do professor e dos alunos da turma. Gostei de fazer esse código pois vi como funciona o programa de organização de uma biblioteca real 