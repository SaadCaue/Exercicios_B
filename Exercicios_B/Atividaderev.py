import sqlite3

def exibir_menu():
  print("Escolha uma opção:")
  print("Sistema de Gerenciamento de Livros")
  print("Menu Principal")
  print("1. Inserir Livro")
  print("2. Consultar Livros")
  print("3. Retirar Livro")
  print("4. Sair")

def inserir_livro():
  nome = input("Qual o nome do livro? ")
  escritor = input("Qual o nome do escritor? ")
  ano = input("Qual o ano de publicação? ")

  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES (?, ?, ?)
  """, (nome, escritor, ano))

  conexao.commit()
  conexao.close()

  print("Livro cadastrado com sucesso!")

def consultar_livros():
  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  SELECT * FROM livros
  """)

  livros = cursor.fetchall()

  conexao.close()

  for livro in livros:
    print("Código:", livro[0])
    print("Nome:", livro[1])
    print("Escritor:", livro[2])
    print("Ano:", livro[3])

def remover_livro():
  codigo = input("Digite o código do livro que deseja retirar: ")

  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  DELETE FROM livros
  WHERE codigo = ?
  """, (codigo,))

  conexao.commit()
  conexao.close()

  print("Livro removido com sucesso!")

if __name__ == "__main__":
  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  CREATE TABLE livros (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    escritor TEXT,
    ano INTEGER
  )
  """)

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES ('Alice no País das Maravilhas', 'Charles Lutwidge Dodgson', 1865)
  """)

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES ('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
  """)

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES ('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997)
  """)

  conexao.commit()
  conexao.close()

  # criando o looping
  while True:
    exibir_menu()

    opcao = int(input())

    if opcao == 1:
      inserir_livro()
    elif opcao == 2:
      consultar_livros()
    elif opcao == 3:
      remover_livro()
    elif opcao == 4:
      print("Saindo...")
      break
