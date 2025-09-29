import sqlite3

# Criação automática do banco e conexão
def conectar():
    conn = sqlite3.connect("estoque.db")
    return conn

# Criação da tabela produtos
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Função para adicionar novo produto
def criar_produto():
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
    except ValueError:
        print("Erro: Quantidade e preço devem ser números.")
        return

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)", 
                       (nome, quantidade, preco))
        conn.commit()
        print("Produto adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: Nome do produto já existe.")
    finally:
        conn.close()

# Função para listar todos os produtos
def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    if produtos:
        print("\nLista de Produtos:")
        print("-" * 40)
        for prod in produtos:
            print(f"ID: {prod[0]} | Nome: {prod[1]} | Quantidade: {prod[2]} | Preço: R$ {prod[3]:.2f}")
    else:
        print("Nenhum produto encontrado.")

# Função para atualizar produto
def atualizar_produto():
    try:
        id = int(input("ID do produto a atualizar: "))
        nova_quantidade = int(input("Nova quantidade: "))
        novo_preco = float(input("Novo preço: "))
    except ValueError:
        print("Erro: Entradas inválidas.")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    if cursor.fetchone():
        cursor.execute("UPDATE produtos SET quantidade = ?, preco = ? WHERE id = ?", 
                       (nova_quantidade, novo_preco, id))
        conn.commit()
        print("Produto atualizado com sucesso.")
    else:
        print("Erro: Produto com ID fornecido não existe.")
    conn.close()

# Função para deletar produto
def deletar_produto():
    try:
        id = int(input("ID do produto a deletar: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conn.commit()
        print("Produto deletado com sucesso.")
    else:
        print("Erro: Produto com ID fornecido não existe.")
    conn.close()

# Menu interativo
def menu():
    criar_tabela()
    while True:
        print("\n==== Sistema de Gerenciamento de Estoque ====")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_produto()
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            atualizar_produto()
        elif escolha == '4':
            deletar_produto()
        elif escolha == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    menu()
