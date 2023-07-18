import textwrap

def menu():
    menu = '''\n
    ############# MENU ###############
    [0]\tDepositar
    [1]\tSacar
    [2]\tExtrato
    [3]\tNova Conta
    [4]\tListar Contas
    [5]\tNovo Usuário
    [6]\tSair
    ############# MENU ###############
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n### Depósito realizado com sucesso! ###")
    else:
        print("\n### Erro na operação! Valor invalido. ####")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeroSaque, limiteSaque):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedido = numeroSaque > limiteSaque

    if saldo_excedido:
        print("\n### Erro de Operação! Saldo Insuficiente. ###")
    
    elif limite_excedido:
        print("\n### Erro de Operação! Limite Excedido!. ###")
    
    elif saques_excedido:
        print("\n### Erro de Operação! Numero de saques excedido. ###")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:2f}\n"
        numeroSaque += 1
        print("\n### Saque realizado com sucesso! ###")
    
    else:
        print("\n### Erro de Operação! ###", menu())
    
    return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):
    print("############### EXTRATO ###############")
    print("Sem movimentações até o momento." if not extrato else extrato)
    print(f"\nSado:\t\tR$ {saldo:2f}")
    print("############### EXTRATO ###############")

def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n### Usuário já existe! Informe outro CPF ###")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço: (rua/av, numero - bairro - cidade/estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("### Usuário criado com sucesso! ###")

def filtrarUsuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Informe seu CPF (somente números 00000000000): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n### Conta criada com sucesso! ###")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario }
    print("\n### Usuário não encontrado! Criação da conta encerrado. ###")

def listarContas(contas):
    for conta in contas:
        linha = f'''\
            Agênvcia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario'['nome']]}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas=[]

    while True:
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numeroSaque = numero_saques,
                limiteSaque = LIMITE_SAQUES,
            )
        elif opcao == "2":
            exibirExtrato(saldo, extrato=extrato)
        elif opcao == "3":
            criarConta(usuarios)
        elif opcao == "4":
            numero_conta = len(contas) -1
            conta = criarConta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "5":
            listarContas(contas)
        elif opcao == "6":
            break
        else:
            print("Operação invalida\n", menu())

main()