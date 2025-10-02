
import BDprova1 as banco

def menu():
    print("\n--- MENU ESTOQUE ---")
    print("1. Inserir produto")
    print("2. Listar produtos")
    print("3. Atualizar produto por ID")
    print("4. Atualizar produtos por categoria")
    print("5. Atualizar produtos por nome")
    print("6. Excluir produto por ID")
    print("7. Excluir produtos por categoria")
    print("8. Excluir produtos por marca")
    print("9. Sair")

def obter_dados_produto():
    nome = input("Nome: ")
    tipo = input("Tipo: ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")
    marca = input("Marca: ")
    return nome, tipo, valor, categoria, marca

if __name__ == "__main__":
    banco.iniciar_banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Inserir Produto ---")
            dados = obter_dados_produto()
            banco.inserir_produto(*dados)

        elif opcao == "2":
            print("\n--- Lista de Produtos ---")
            banco.listar_produtos()

        elif opcao == "3":
            print("\n--- Atualizar por ID ---")
            id_produto = int(input("ID do produto: "))
            dados = obter_dados_produto()
            banco.atualizar_produto_por_id(id_produto, *dados)

        elif opcao == "4":
            print("\n--- Atualizar por Categoria ---")
            categoria_antiga = input("Categoria atual: ")
            dados = obter_dados_produto()
            banco.atualizar_produtos_por_categoria(categoria_antiga, *dados)

        elif opcao == "5":
            print("\n--- Atualizar por Nome ---")
            nome_antigo = input("Nome atual: ")
            dados = obter_dados_produto()
            banco.atualizar_produtos_por_nome(nome_antigo, *dados)

        elif opcao == "6":
            print("\n--- Excluir por ID ---")
            id_produto = int(input("ID do produto: "))
            banco.excluir_produto_por_id(id_produto)

        elif opcao == "7":
            print("\n--- Excluir por Categoria ---")
            categoria = input("Categoria: ")
            banco.excluir_produtos_por_categoria(categoria)

        elif opcao == "8":
            print("\n--- Excluir por Marca ---")
            marca = input("Marca: ")
            banco.excluir_produtos_por_marca(marca)

        elif opcao == "9":
            print("Encerrando...")
            banco.fechar_banco()
            break

        else:
            print("Opção inválida. Tente novamente.")
