texto_a_repetir = input("Digite o texto a repetir: ")
while True:
    try:
        vezes_a_repetir = int(input("digite o número de vezes a repetir: "))
        break
    except:
        print("por favor insira um número")
print((texto_a_repetir + " ") * vezes_a_repetir)