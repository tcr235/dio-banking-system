def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"

    else:
        print("Operação não concluída: o valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (valor > saldo):
        print("Operação não concluída: não há saldo suficiente em conta.")

    elif (valor > limite):
        print("Operação não concluída: você excedeu o limite máximo de saque.")

    elif (numero_saques > limite_saques):
        print("Operação não concluída: você excedeu o limite máximo de saques diários.")

    elif (valor > 0):
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação não concluída: o valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=========== EXTRATO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("=================================")

def criar_usuario():
    pass

def filtrar_usuario():
    pass

def criar_conta():
    pass

def listar_contas():
    pass

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if (opcao == "d"):
            valor = float(input("Digite o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif (opcao == "s"):
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif (opcao == "e"):
            exibir_extrato(saldo, extrato=extrato)

        elif (opcao == "q"):
            break

        else:
            print("Operação inválida, por favor digite novamente a operação desejada.")

main()