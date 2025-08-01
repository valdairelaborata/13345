

while True:
    try:
        valor = int(input("Informe um número: "))
        if valor == 0:
            print("Infinito")
            continue

        else:
            resultado = 1 / valor
            print(f"Resultado: {resultado}")
            
        break
    except ValueError:
        print("Valor inválido, informe um valor válido")

    except:
        print("Erro")