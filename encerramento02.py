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