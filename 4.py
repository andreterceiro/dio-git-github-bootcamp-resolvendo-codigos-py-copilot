while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except:
        print("Por favor digite um número")

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")