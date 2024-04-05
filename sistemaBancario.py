menu = '''[D]-Depósito\n[S]-Saque\n[E]-Extrato\n[Q]-Sair\n=> '''

saldo = 2000
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
'''
# Lista de usuários

lista_usuario = []
usuarios = {'nome':'', 'dat_nascimetno':'', 'cpf':'', 'endereço':'' }

# Função para criar novos usuários
def criarar_usuario():
    pass

# Função para criar uma nova conta corrente
def criar_conta_corrente():
    pass'''


while True:

    opcao = input(menu)
    opcao.lower()

    if opcao == 'd':
        valor = float(input('Depósito\nInforme o valor: '))
        
        if valor > 0: # garantindo que não haja valores neagativos
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else: # caso o valor informado seja negativo
            print('Operação falhou! O valor informado é inválido.')


    elif opcao == 's':
        valor = float(input(f'Saque\nIforme o valor: '))

        # Comparação booleana
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido')

    elif opcao == 'e':
        print('\nxxxxxxxx EXTRATO xxxxxxxx')
        print('Não foram realizado movimentações.' if not extrato else extrato)
        print(f'\nSaldo da conta: R$ {saldo:.2f}')

    elif opcao == 'q':
        break

    elif numero_saques == 3:
        print('Número de saques por dia atingido')
        break

    else:
        print('Operação inválida, por favor selecione novamente')