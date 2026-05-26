def solicitar_idade_valida():

    idade = 0
    
    while True:
        try:
            entrada = input("Por favor, insira a sua idade: ")
            idade = int(entrada)
            
            if idade <= 0:
                raise ValueError("A idade deve ser um número positivo (maior que zero).")

            break
            
        except ValueError as e:
            print(f"\nERRO de Validação: {e}. Por favor, tente novamente.")
            
    print(f"\nIdade validada com sucesso! Você tem {idade} anos.")
    return idade

if __name__ == "__main__":
    solicitar_idade_valida()