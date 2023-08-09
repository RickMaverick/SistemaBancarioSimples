import datetime
menu = '''

[d] depositar
[s] sacar
[e] extrato
[q] sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print("DEPÓSITO")
        valor_deposito = float(input("Digite a quantia a ser depositada: "))
        saldo += valor_deposito
        extrato +=f"\nDepósito: R${valor_deposito} - {datetime.date.today()}"
        print("Depósito realizado com sucesso!")


    elif opcao == 's':
        print("SAQUE")
        valor_sacar = float(input("Digite a quantia a ser sacada: "))

        if numero_de_saques>=3:
            print("Não é possivel realizar mais de 3 saques ao dia. Tente novamente amanhã.")
        elif valor_sacar>500:
            print("Não é possivel sacar valores maiores que R$500,00 de uma vez.")
        elif valor_sacar<=0:
            print("Operação Indisponivel. Realize apenas saques de valores positivos.")
        else:
            if saldo>=valor_sacar:
                saldo-=valor_sacar
                print("Saque realizado com sucesso!")
                extrato += f"\nSaque: R${valor_sacar} - {datetime.date.today()}"
                numero_de_saques+=1
            else:
                print("Saque indisponivel. Confira seu saldo.")


    elif opcao == 'e':
        if saldo>0 or numero_de_saques!=0:
            print("EXTRATO")
            print(extrato)
            print('-'*40)
            print(f"SALDO: R${saldo:.2f}")
        else:
            print("EXTRATO")
            print("Não foram realizadas movimentações.")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada...")