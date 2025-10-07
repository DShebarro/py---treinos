import matplotlib.pyplot as plt

# Dados

class Livro:
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel

    def __str__(self):
        return (f"Título: {self.titulo} | Autor: {self.autor} | Genero: {self.genero} |" 
                f"Disponível: {self.quantidade_disponivel} ")


lista_livros = []

def cadastrar_livro():
    print("\n---- Cadastro de Livros ----")
    titulo = input("Título: ").strip().title()
    autor = input("Autor: ").strip().title()
    genero = input("Gênero: ").strip().title()

    while True:
        try:
            quantidade = int(input("Quantidade Disponível: ").strip())
            if quantidade >= 0:
                break
            else:
                print("A quantidade deve ser um número não negativo")
        except ValueError:
            print("Entrada Inválida. Por favor, digite um número inteiro")

    novo_livro = Livro(titulo, autor, genero, quantidade)

    lista_livros.append(novo_livro)
    print(f"\n Livro '{titulo}' foi cadastrado!")

def listar_livros():
    if not lista_livros:
        print("\n Não tem livros cadastrados na biblioteca.")
        return

    print("\n---- Lista de Livros disponível na biblioteca ----")
    for i, livro in enumerate(lista_livros):
        print(f"[{i+1}] {livro}")
    print("-" * 40)

def buscar_livro_em_titulo():
    if not lista_livros:
        print("\n Não tem livros para buscar")
        return
    
    titulo_busca = input("\n Digite o Título do livro que deseja encontrar: ").strip().title()

    encontrados = [livro for livro in lista_livros if titulo_busca in livro.titulo]

    if encontrados:
        print(f"\n --- Resultado de Busca por '{titulo_busca}' ---")
        for livro in encontrados:
            print(livro)
    else:
        print(f"\n Livro com título '{titulo_busca}' não foi encontrado na biblioteca.")

def gerar_grafico_de_genero():
    if not lista_livros:
        print("\n Não foi possível gerar gráfico. Sem livros cadastrados.")
        return

    contagem_genero = {}
    for livro in lista_livros:
        genero = livro.genero
        quantidade = livro.quantidade_disponivel

        contagem_genero[genero] = contagem_genero.get(genero, 0) + quantidade

    generos = list(contagem_genero.keys())
    quantidade = list(contagem_genero.values())

    plt.figure(figsize = (10, 6))
    barras = plt.bar(generos, quantidade, color='skyblue')

    plt.xlabel('Genero')
    plt.ylabel('Quantidade Total de Livros')
    plt.title('Quantidade de Livros por Gênero na Biblioteca')
    plt.xticks(rotation = 45, ha='right')
    plt.grid(axis='y', linestyle ='--', alpha=0.7)

    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.1, round(yval), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
    print