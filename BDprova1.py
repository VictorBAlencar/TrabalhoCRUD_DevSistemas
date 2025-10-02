
import sqlite3

conexao = sqlite3.connect("Estoque.db")
cursor = conexao.cursor()

def iniciar_banco():
  conexao = sqlite3.connect("Estoque.db")
  cursor = conexao.cursor()
  
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS produtos(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT UNIQUE NOT NULL,
      tipo TEXT NOT NULL,
      valor REAL NOT NULL,
      categoria TEXT NOT NULL,
      marca TEXT NOT NULL                        
      )
  """)

def inserir_produto(nome,tipo,valor,categoria,marca):
    try:
        cursor.execute("INSERT INTO produtos (nome,tipo,valor,categoria,marca) VALUES(?,?,?,?,?)", 
                       (nome,tipo,valor,categoria,marca))
        conexao.commit()
        print("Produto inserido com sucesso")
    except sqlite3.IntegrityError:
        print("Erro: Produto já existente")

def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for i in produtos:
        print(i)

def atualizar_produto(id_produto,novo_nome,novo_tipo, novo_valor,nova_categoria, nova_marca):
    cursor.execute("UPDATE produtos SET nome =?, tipo=?,valor=?,categoria=?,marca=?, WHERE id=?",
     (novo_nome,novo_tipo, novo_valor,nova_categoria,nova_marca,id_produto))
    
    if cursor.rowcount > 0:
        print("Produto atualizado com sucesso!")
        conexao.commit()
    else:
        print("Produto não encontrado!")

    cursor.execute("UPDATE produtos SET nome =?, tipo=?,valor=?,categoria=?,marca=?, WHERE categoria=?",
     (novo_nome,novo_tipo, novo_valor,nova_categoria,nova_marca,id_produto))

def excluir_produto(id_produto):
    cursor.execute("DELETE FROM produtos WHERE id = ?",(id_produto,))

    if cursor.rowcount > 0:
        print("Produto excluido com sucesso!")
        conexao.commit()
    else:
        print("Produto não encontrado!")

    cursor.execute("DELETE FROM produtos WHERE categoria = ?")

def fechar_banco():
    conexao.commit()
    conexao.close()
