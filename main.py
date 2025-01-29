import calcula_soma
import fibonacci
import calcula_faturamento
import calcula_percentual
import inverte_string

def mostrar_menu():
    print("Escolha uma opção:")
    print("1. Calcular soma")
    print("2. Verificar número na sequência de Fibonacci")
    print("3. Calcular faturamento diário")
    print("4. Calcular percentual de faturamento por estado")
    print("5. Inverter string")
    print("0. Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            calcula_soma.calcular_soma()
        elif opcao == "2":
            fibonacci.verificar_fibonacci()
        elif opcao == "3":
            calcula_faturamento.calcular_faturamento_diario()
        elif opcao == "4":
            calcula_percentual.calcular_percentual_faturamento()
        elif opcao == "5":
            inverte_string.inverter_string()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
