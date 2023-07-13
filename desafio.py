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
            