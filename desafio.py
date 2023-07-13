menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if (opcao == "d"):
        valor = float(input("Digite o valor a ser depositado: "))

        if (valor > 0):
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Operação não concluída: o valor informado é inválido.")

    elif (opcao == "s"):
        valor = float(input("Informe o valor do saque: "))
        
        if (valor > saldo):
            print("Operação não concluída: não há saldo suficiente em conta.")

        elif (valor > limite):
            print("Operação não concluída: você excedeu o limite máximo de saque.")

        elif (numero_saques > LIMITE_SAQUES):
            print("Operação não concluída: você excedeu o limite máximo de saques diários.")

        elif (valor > 0):
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não concluída: o valor informado é inválido.")
