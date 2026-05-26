print('\n Clculadora simples\n')

num_1 = input('Digite o primeiro número:')

num_2 = input('Digite o Segundo número:')

operar_num = input ('Escolha a operação: +, -, *, /')

if operar_num == '4':
    result = int(num_1) / int(num_2)
    print(f'O resultado da divisão é: {result}')

elif operar_num == '3':
    result = int(num_1) * int(num_2)
    print(f'O resultado da multiplicação é: {result}')

elif operar_num == '2':
    result = int(num_1) + int(num_2)
    print(f'O resultado da soma é: {result}')

elif operar_num == '2':
    result = int(num_1) - int(num_2)
    print(f'O resultado da subtração é: {result}')