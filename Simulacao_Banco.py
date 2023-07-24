def main():
    # Pergunta se o usuário já tem conta
    has_account = input("Você já tem uma conta bancária? (S/N): ").upper()

    if has_account == "S":
        saldo = 1000  # Saldo inicial para quem já possui conta
    elif has_account == "N":
        saldo = float(input("Digite o valor inicial para abrir a conta: "))
    else:
        print("Opção inválida. Encerrando o programa.")
        return

    while True:
        print("\nEscolha uma opção:")
        print("1 - Verificar saldo")
        print("2 - Fazer depósito")
        print("3 - Fazer saque")
        print("4 - Solicitar empréstimo/financiamento")
        print("0 - Encerrar o programa")

        opcao = int(input("Opção: "))

        if opcao == 0:
            print("Encerrando o programa.")
            break
        elif opcao == 1:
            print(f"Seu saldo atual é R$ {saldo:.2f}")
        elif opcao == 2:
            deposito = float(input("Digite o valor do depósito: "))
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado. Seu saldo atual é R$ {saldo:.2f}")
        elif opcao == 3:
            saque = float(input("Digite o valor do saque: "))
            if saque <= saldo:
                saldo -= saque
                print(f"Saque de R$ {saque:.2f} realizado. Seu saldo atual é R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente. Operação não realizada.")
        elif opcao == 4:
            salario = float(input("Digite sua renda: "))
            valor_liberado = salario * 35 / 100 * 12
            print(f"Valor liberado: R$ {valor_liberado:.2f}")

            valor_solicitado = float(input("Digite o valor do empréstimo desejado: "))
            if valor_solicitado > valor_liberado:
                print(f"Valor solicitado maior que o valor máximo disponibilizado. O valor disponibilizado é de R$ {valor_liberado:.2f}")
            else:
                parcelas = int(input("Digite em quantas parcelas deseja pagar (1 até 12): "))
                while parcelas > 12 or parcelas == 0:
                    print("Número de parcelas deve ser entre 1 e 12.")
                    parcelas = int(input("Digite em quantas parcelas deseja pagar: "))

                if parcelas == 1:
                    taxa_juros = 0
                elif 2 <= parcelas <= 5:
                    taxa_juros = 3.5
                elif 6 <= parcelas <= 8:
                    taxa_juros = 5
                else:
                    taxa_juros = 9

                valor_final = valor_solicitado * (1 + taxa_juros / 100)
                valor_parcela = valor_final / parcelas

                print(f"Valor total do empréstimo (com juros): R$ {valor_final:.2f}")
                print(f"Taxa de Juros: {taxa_juros:.2f} %")
                print(f"{parcelas} parcelas mensais de: R$ {valor_parcela:.2f}")
        
        else:
            print("Opção inválida. Tente novamente.")

        fazer_outra_operacao = input("Deseja fazer outra operação? (S/N): ").upper()
        if fazer_outra_operacao != "S":
            break


if __name__ == "__main__":
    main()
    