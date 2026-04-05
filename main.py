# Calculadora em Python

def calculadora():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Digite apenas números.\n")
            continue

        print("\nEscolha a operação:")
        print("1. Adição") 
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")

        operacao = input("Digite o número da operação desejada: ")

        if operacao == '1':
            resultado = numero1 + numero2
            print(f"Resultado: {resultado}")

        elif operacao == '2':
            resultado = numero1 - numero2
            print(f"Resultado: {resultado}")

        elif operacao == '3':
            resultado = numero1 * numero2
            print(f"Resultado: {resultado}")   

        elif operacao == '4':
            if numero2 != 0:
                resultado = numero1 / numero2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: divisão por zero.\n")
                continue

        else:
            print("Operação inválida.\n")
            continue

        continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando calculadora...")
            break

# Executar
print("CALCULADORA INICIADA\n")
calculadora()