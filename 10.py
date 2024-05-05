import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("livros.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        autor TEXT,
        ano INTEGER
    )
    """)

    conexao.commit()
    conexao.close()

def adicionar_livro(titulo, autor, ano):
    conexao = sqlite3.connect("livros.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)", (titulo, autor, ano))

    conexao.commit()
    conexao.close()

def remover_livro(id_livro):
    conexao = sqlite3.connect("livros.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM livros WHERE id=?", (id_livro,))

    conexao.commit()
    conexao.close()

def consultar_livros():
    conexao = sqlite3.connect("livros.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    conexao.close()
    return livros

criar_tabela()

adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e Preconceito", "Jane Austen", 1813)
adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)

print("Lista de Livros:")
for livro in consultar_livros():
    print(livro)

remover_livro(2)

print("\nLista de Livros após a remoção:")
for livro in consultar_livros():
    print(livro)
