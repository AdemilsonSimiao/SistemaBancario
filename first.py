menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 5

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = int(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro na operação! O valor informado é invalido.")

    elif opcao == "s":
        valor = int(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro! Saldo insulficiente")
        elif excedeu_limite:
            print("Erro! Valor do saque execede o Limite.")
        elif excedeu_saques:
            print("Erro! Numero de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Erro! Valor informado invalido.")

    elif opcao == "e":
        print("\n ======Extrato======")
        print("Não foi realizado movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("========Extrato========")

    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Opção invalida, por favor selecione uma das opções: D para deposito, S para saque, E para Extrato ou Q para sair")