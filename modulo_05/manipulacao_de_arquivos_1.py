import csv
import os
caminho_pasta = "C:\Users\pandr\Desktop\curso\CODIGO_DA_TRANSFORMAÇÃO_joao_victor_EAD\modulo_4"
nome_arquivo = "notas.csv"
caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

def adicionar_nota(aluno, nota):
    with open(caminho_completo, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([aluno, nota])
    print(f"✅ Nota de '{aluno}' adicionada com sucesso!")

def carregar_notas():
    if not os.path.exists(caminho_completo):
        print("📝 O arquivo de notas ainda não foi criado.")
        return

    with open(caminho_completo, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        print("\n--- Notas Salvas ---")
        for linha in leitor_csv:
            aluno = linha[0]
            nota = linha[1]
            print(f"Aluno: {aluno}, Nota: {nota}")
    print("--------------------")

while True:
    print("\n--- Menu do Sistema de Notas ---")
    print("1. Adicionar nota")
    print("2. Visualizar notas")
    print("3. Sair")
    
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        aluno = input("Nome_Aluno")
        nota = input("Nota_Aluno")
        adicionar_nota(aluno, nota)
        
    elif escolha == '2':
        carregar_notas()
            
    elif escolha == '3':
        print("Saindo do sistema. Até a próxima!")
        break
        
    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")