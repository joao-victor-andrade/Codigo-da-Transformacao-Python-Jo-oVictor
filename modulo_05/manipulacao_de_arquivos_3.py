import csv
import os
import shutil
caminho_principal = "C:\Users\pandr\Desktop\curso\CODIGO_DA_TRANSFORMAÇÃO_joao_victor_EAD\modulo_4"
caminho_backup = "C:\Users\pandr\Desktop\curso\CODIGO_DA_TRANSFORMAÇÃO_joao_victor_EAD\modulo_4\backup"
nome_arquivo = "notas.csv"
caminho_completo = os.path.join(caminho_principal, nome_arquivo)
def adicionar_nota(aluno, nota):
    with open(caminho_completo, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([aluno, nota])
    print(f"Nota de '{aluno}' adicionada com sucesso!")

def carregar_notas():
    if not os.path.exists(caminho_completo):
        print("O arquivo de notas ainda não existe.")
        return

    with open(caminho_completo, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        print("\n--- Notas Salvas ---")
        for linha in leitor_csv:
            aluno = linha[0]
            nota = linha[1]
            print(f"Aluno: {aluno}, Nota: {nota}")
    print("--------------------")

def fazer_backup():
    if not os.path.exists(caminho_completo):
        print("Erro: O arquivo de notas não existe. Adicione uma nota primeiro.")
        return
    
    os.makedirs(caminho_backup, exist_ok=True)
    
    caminho_backup_completo = os.path.join(caminho_backup, nome_arquivo)
    
    try:
        shutil.copy2(caminho_completo, caminho_backup_completo)
        print(f"Backup do arquivo '{nome_arquivo}' concluído com sucesso!")
        print(f"O backup foi salvo em: {caminho_backup_completo}")
    except Exception as e:
        print(f"Ocorreu um erro ao fazer o backup: {e}")

while True:
    print("\n--- Sistema de Notas com Backup ---")
    print("1. Adicionar nota")
    print("2. Visualizar notas")
    print("3. Fazer Backup das Notas")
    print("4. Sair")
    
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        aluno = input("Nome do aluno: ")
        nota = input("Nota do aluno: ")
        adicionar_nota(aluno, nota)
        
    elif escolha == '2':
        carregar_notas()
            
    elif escolha == '3':
        fazer_backup()
        
    elif escolha == '4':
        print("Saindo do sistema. Até a próxima!")
        break
        
    else:
        print("Opção inválida. Por favor, digite 1, 2, 3 ou 4.")