import os
caminho_pasta = "C:\Users\pandr\Desktop\curso\CODIGO_DA_TRANSFORMAÇÃO_joao_victor_EAD\modulo_4"
nome_arquivo = "meu_primeiro_arquivo.txt"
caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

print("--- Escrevendo no arquivo... ---")
with open(caminho_completo, 'w') as arquivo:
    arquivo.write("Olá, este é o meu primeiro arquivo de texto criado com Python!\n")
    arquivo.write("Estou aprendendo a salvar informações. Que legal!\n")
    print("Conteúdo escrito com sucesso!")
print("\n--- Lendo o conteúdo do arquivo... ---")

with open(caminho_completo, 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo lido:")
    print(conteudo)