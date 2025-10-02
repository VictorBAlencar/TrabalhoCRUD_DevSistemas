
import sqlite3

conexao = sqlite3.connect("Estoque.db")
cursor = conexao.cursor()

def iniciar_banco():
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
    conexao.commit()

def inserir_produto(nome, tipo, valor, categoria, marca):
    try:
        cursor.execute("INSERT INTO produtos (nome, tipo, valor, categoria, marca) VALUES (?, ?, ?, ?, ?)", 
                       (nome, tipo, valor, categoria, marca))
        conexao.commit()
        print("Produto inserido com sucesso")
    except sqlite3.IntegrityError:
        print("Erro: Produto já existente")

def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)

def atualizar_produto_por_id(id_produto, novo_nome, novo_tipo, novo_valor, nova_categoria, nova_marca):
    cursor.execute("""
        UPDATE produtos
        SET nome = ?, tipo = ?, valor = ?, categoria = ?, marca = ?
        WHERE id = ?
    """, (novo_nome, novo_tipo, novo_valor, nova_categoria, nova_marca, id_produto))
    
    if cursor.rowcount > 0:
        print("Produto atualizado com sucesso!")
        conexao.commit()
    else:
        print("Produto não encontrado!")

def atualizar_produtos_por_categoria(categoria_antiga, novo_nome, novo_tipo, novo_valor, nova_categoria, nova_marca):
    cursor.execute("""
        UPDATE produtos
        SET nome = ?, tipo = ?, valor = ?, categoria = ?, marca = ?
        WHERE categoria = ?
    """, (novo_nome, novo_tipo, novo_valor, nova_categoria, nova_marca, categoria_antiga))
    
    if cursor.rowcount > 0:
        print("Produtos da categoria atualizados com sucesso!")
        conexao.commit()
    else:
        print("Nenhum produto encontrado para essa categoria!")

def atualizar_produtos_por_nome(nome_antigo, novo_nome, novo_tipo, novo_valor, nova_categoria, nova_marca):
    cursor.execute("""
        UPDATE produtos
        SET nome = ?, tipo = ?, valor = ?, categoria = ?, marca = ?
        WHERE nome = ?
    """, (novo_nome, novo_tipo, novo_valor, nova_categoria, nova_marca, nome_antigo))
    
    if cursor.rowcount > 0:
        print("Produtos com esse nome atualizados com sucesso!")
        conexao.commit()
    else:
        print("Nenhum produto encontrado com esse nome!")

def excluir_produto_por_id(id_produto):
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    if cursor.rowcount > 0:
        print("Produto excluído com sucesso!")
        conexao.commit()
    else:
        print("Produto não encontrado!")

def excluir_produtos_por_categoria(categoria):
    cursor.execute("DELETE FROM produtos WHERE categoria = ?", (categoria,))
    if cursor.rowcount > 0:
        print("Produtos excluídos com sucesso!")
        conexao.commit()
    else:
        print("Nenhum produto encontrado para essa categoria!")

def excluir_produtos_por_marca(marca):
    cursor.execute("DELETE FROM produtos WHERE marca = ?", (marca,))
    if cursor.rowcount > 0:
        print("Produtos excluídos com sucesso!")
        conexao.commit()
    else:
        print("Nenhum produto encontrado dessa marca!")

def fechar_banco():
    conexao.commit()
    conexao.close()
