import json
import os

nome_arquivo_json = "clientes.json"
def adicionar_cliente():
    clientes = {}
    if os.path.exists(nome_arquivo_json):
        with open(nome_arquivo_json, 'r') as arquivo_json:
            clientes = json.load(arquivo_json)

    print("\n--- Adicionar Novo Cliente ---")
    nome = input("Digite o nome do cliente: ")
    if nome in clientes:
        print(f"Erro: O cliente '{nome}' já existe na base de dados.")
        return

    cliente_id = input("Digite o ID do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    clientes[nome] = {
        "id": cliente_id,
        "cidade": cidade
    }
    with open(nome_arquivo_json, 'w') as arquivo_json:
        json.dump(clientes, arquivo_json, indent=4)
        
    print(f"Cliente '{nome}' adicionado e salvo com sucesso!")

def visualizar_clientes():
    if not os.path.exists(nome_arquivo_json):
        print("O arquivo de clientes ainda não existe.")
        return

    # Carrega os dados do arquivo.
    with open(nome_arquivo_json, 'r') as arquivo_json:
        clientes = json.load(arquivo_json)
    
    if not clientes:
        print("A lista de clientes está vazia.")
        return

    print("\n--- Lista de Clientes ---")
    for nome, detalhes in clientes.items():
        print(f"Nome: {nome}")
        print(f"  ID: {detalhes['id']}")
        print(f"  Cidade: {detalhes['cidade']}")
        print("-------------------------")
while True:
    print("\n--- Menu do Gerenciador de Clientes ---")
    print("1.Adicionar cliente")
    print("2.Visualizar clientes")
    print("3.Sair")
    
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        adicionar_cliente()
    elif escolha == '2':
        visualizar_clientes()
    elif escolha == '3':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")