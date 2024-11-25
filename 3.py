while True:
    try:
        valor1 = int(input("Digite o valor 1: "))
        break
    except:
        print("Erro! Por favor, digite um número.")

while True:
    try:
        valor2 = int(input("Digite o valor 2: "))
        break
    except:
        print("Erro! Por favor, digite um número.")

operacao = input("Por favor insira a operacao matemática (+ ou - ou * ou /): ")

if operacao == "+":
    print(f"O resultado da operação é: {valor1 + valor2}")
elif operacao == "-":
    print(f"O resultado da operação é: {abs(valor1 - valor2)}")
elif operacao == "*":
    print(f"O resultado da operação é: {valor1 * valor2}")
elif operacao == "/":
    print(f"O resultado da operação é: {valor1 / valor2}")
else:
    print("Operacao inválida!")

