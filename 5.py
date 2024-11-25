while(True):
    try:
        nota1 = float(input("Por favor insira a nota 1: "))
        break
    except:
        print("Pr favor insira um número. O separador decimal deve ser '.'")

while(True):
    try:
        nota2 = float(input("Por favor insira a nota 2: "))
        break        
    except:
        print("Pr favor insira um número. O separador decimal deve ser '.'")

while(True):
    try:
        nota3 = float(input("Por favor insira a nota 3: "))
        break        
    except:
        print("Pr favor insira um número. O separador decimal deve ser '.'")

print((nota1 + nota2 + nota3)/3)
