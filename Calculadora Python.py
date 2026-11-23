
print("Calculadora simples.")

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Não é possível dividir por zero"
    else:
        return a / b

def menu():
    print("\n================================")
    print("       Calculadora Simples")
    print("================================")
    print(" 1 - Adição (+)")
    print(" 2 - Subtração (-)")
    print(" 3 - Multiplicação (*)")
    print(" 4 - Divisão (/)")
    print(" 5 - Sair")

while True:
    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "5":
        print("Obrigado por utilizar a calculadora!")
        break

    elif opcao in ["1", "2", "3", "4"]:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = adicao(numero1, numero2)

        elif opcao == "2":
            resultado = subtracao(numero1, numero2)

        elif opcao == "3":
            resultado = multiplicacao(numero1, numero2)

        elif opcao == "4":
            resultado = divisao(numero1, numero2)

        print("Resultado:", resultado)
        print("/n1  - Voltar para a calculadora.")
        print("/n2  -Sair.")

        voltar= input("Escolha uma opcao: ")

        if voltar=="2":
         print("Obrigado por utilizar!")
         break
        elif voltar=="1":
            continue

    
print("Calculadora simples.")

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Não é possível dividir por zero"
    else:
        return a / b

def menu():
    print("\n================================")
    print("       Calculadora Simples")
    print("================================")
    print(" 1 - Adição (+)")
    print(" 2 - Subtração (-)")
    print(" 3 - Multiplicação (*)")
    print(" 4 - Divisão (/)")
    print(" 5 - Sair")

while True:
    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "5":
        print("Obrigado por utilizar a calculadora!")
        break

    elif opcao in ["1", "2", "3", "4"]:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = adicao(numero1, numero2)

        elif opcao == "2":
            resultado = subtracao(numero1, numero2)

        elif opcao == "3":
            resultado = multiplicacao(numero1, numero2)

        elif opcao == "4":
            resultado = divisao(numero1, numero2)

        print("Resultado:", resultado)

    else:
        print("Opção inválida!Voltando ao menu...")
        continue
    
else:
        print("Opção inválida! Tente novamente.")

 
    
    


