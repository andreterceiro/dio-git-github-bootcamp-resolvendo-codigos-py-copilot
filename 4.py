while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except:
        print("Por favor digite um número")

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
