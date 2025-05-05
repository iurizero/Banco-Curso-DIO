def menu():
    print("\n=== MENU ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")
    return input("Escolha uma opção: ")

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Valor inválido para depósito.")
    return saldo

def sacar(saldo, extrato, saques_realizados, limite=500, max_saques=3):
    if saques_realizados >= max_saques:
        print("❌ Limite de saques diários atingido (3 por dia).")
        return saldo, saques_realizados

    valor = float(input("Informe o valor do saque: "))

    if valor <= 0:
        print("❌ Valor inválido para saque.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print(f"❌ Limite de R$ {limite} por saque excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_realizados += 1
        print("✅ Saque realizado com sucesso!")

    return saldo, saques_realizados

def mostrar_extrato(extrato, saldo):
    print("\n=== EXTRATO ===")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def main():
    saldo = 2000
    extrato = []
    saques_realizados = 0

    while True:
        opcao = menu()

        if opcao == "1":
            saldo = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, saques_realizados = sacar(saldo, extrato, saques_realizados)
        elif opcao == "3":
            mostrar_extrato(extrato, saldo)
        elif opcao == "0":
            print("✅ Encerrando o sistema. Obrigado por usar nosso banco!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
