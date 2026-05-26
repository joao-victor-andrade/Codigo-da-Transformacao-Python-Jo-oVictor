def media(notas):
    nota_minima_para_aprovar = 6.0
    if not notas:
        return "Nenhuma nota fornecida."
    media = sum(notas) / len(notas)

    print(f"A média do aluno é: {media:.2f}")
    if media >= nota_minima_para_aprovar:
        return "Aprovado"
    else:
        return "Reprovado"

print("--- Cenário 1: Aluno Aprovado ---")
notas_aluno1 = [7.0, 6.5, 9.0]
resultado1 = media(notas_aluno1)
print(f"Resultado: {resultado1}\n")

print("--- Cenário 2: Aluno Reprovado ---")
notas_aluno2 = [5.5, 5.0, 6.5]
resultado2 = media(notas_aluno2)
print(f"Resultado: {resultado2}\n")

print("--- Cenário 3: Lista de notas vazia ---")
notas_aluno3 = []
resultado3 = media(notas_aluno3)
print(f"Resultado: {resultado3}")