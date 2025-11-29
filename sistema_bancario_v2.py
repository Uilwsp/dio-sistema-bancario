# SISTEMA BANCÁRIO
# - Cadastro de usuários
# - Cadastro de contas
# - Depósitos, saques e extratos por conta


usuarios = []
contas = []

# CRIAR USUÁRIO

def criar_usuario(usuarios):
  
    cpf = input("CPF (somente números): ")

  
    for user in usuarios:
        if user["cpf"] == cpf:
            print("❌ CPF já cadastrado! Usuário não criado.")
            return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")

    logradouro = input("Endereço (Rua, Avenida, etc.): ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("UF: ")

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("✔ Usuário criado com sucesso!")


# LISTAR USUÁRIOS

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print("=== Usuário ===")
        print(f"Nome: {usuario['nome']}")
        print(f"Nascimento: {usuario['data_nascimento']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereço: {usuario['endereco']}")
        print()


# FILTRAR USUÁRIO POR CPF

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


# CRIAR CONTA

def criar_conta_corrente(contas, usuarios, agencia="001"):
    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("❌ Usuário não encontrado. Conta não criada.")
        return

    numero_conta = len(contas) + 1  # número sequencial

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "limite": 500,
        "saques": 0,
        "limite_saques": 3
    }

    contas.append(conta)
    print("✔ Conta criada com sucesso!")
    print(f"Agência: {agencia}")
    print(f"Conta: {numero_conta}")
    print(f"Cliente: {usuario['nome']}")


# LISTAR CONTAS

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Cliente: {conta['usuario']['nome']}")


# BUSCAR CONTA PELO NÚMERO

def buscar_conta(numero_conta, contas):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    return None


# DEPÓSITO

def depositar(conta):
    valor = float(input("Valor do depósito: "))

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print("✔ Depósito realizado!")
    else:
        print("❌ Valor inválido.")


# SAQUE

def sacar(conta):
    valor = float(input("Valor do saque: "))

    if valor <= 0:
        print("❌ Valor inválido.")
        return

    if valor > conta["saldo"]:
        print("❌ Saldo insuficiente.")
        return

    if valor > conta["limite"]:
        print("❌ Saque acima do limite permitido.")
        return

    if conta["saques"] >= conta["limite_saques"]:
        print("❌ Limite diário de saques atingido.")
        return

    conta["saldo"] -= valor
    conta["saques"] += 1
    conta["extrato"].append(f"Saque: R$ {valor:.2f}")
    print("✔ Saque realizado!")



# EXTRATO

def mostrar_extrato(conta):
    print("\n========== EXTRATO ==========")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for mov in conta["extrato"]:
            print(mov)

    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("==============================\n")



# MENU PRINCIPAL

while True:
    print("\n======= MENU PRINCIPAL =======")
    print("[1] Criar usuário")
    print("[2] Criar conta")
    print("[3] Listar usuários")
    print("[4] Listar contas")
    print("[5] Acessar conta")
    print("[0] Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        criar_usuario(usuarios)

    elif opcao == "2":
        criar_conta_corrente(contas, usuarios)

    elif opcao == "3":
        listar_usuarios(usuarios)

    elif opcao == "4":
        listar_contas(contas)

    elif opcao == "5":
        numero = int(input("Número da conta: "))
        conta = buscar_conta(numero, contas)

        if not conta:
            print("❌ Conta não encontrada.")
            continue

        # MENU DA CONTA
        while True:
            print("\n======= MENU DA CONTA =======")
            print("[d] Depositar")
            print("[s] Sacar")
            print("[e] Extrato")
            print("[v] Voltar")
            acao = input("Escolha: ")

            if acao == "d":
                depositar(conta)
            elif acao == "s":
                sacar(conta)
            elif acao == "e":
                mostrar_extrato(conta)
            elif acao == "v":
                break
            else:
                print("Opção inválida.")

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida.")
