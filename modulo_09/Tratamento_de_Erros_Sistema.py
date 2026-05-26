MAX_TENTATIVAS = 3
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "123456"

class LoginInvalidoError(Exception):
    pass

def verificar_credenciais(usuario, senha):
    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        return True
    else:
        raise LoginInvalidoError("Nome de utilizador ou palavra-passe incorretos.")

def sistema_login():
    print("--- Sistema de Login ---")
    
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        print(f"\nTentativa {tentativa} de {MAX_TENTATIVAS}:")
        
        try:
            usuario_input = input("Nome de utilizador: ")
            senha_input = input("Palavra-passe: ")
            
            if verificar_credenciais(usuario_input, senha_input):
                print("\nLOGIN BEM-SUCEDIDO! Bem-vindo(a)!")
                return
                
        except LoginInvalidoError as e:
            print(f"erro: {e}")
            if tentativa == MAX_TENTATIVAS:
                print("\nNúmero máximo de tentativas atingido. Acesso bloqueado.")
                return
            
if __name__ == "__main__":
    sistema_login()