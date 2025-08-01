
def validar_divisao():
    valor_valido = False
    resultado = None

    while valor_valido == False:
        try:
            valor = int(input("Informe um número: "))
            if valor == 0:
                print("Infinito")

            else:
                resultado =  1 / valor
                valor_valido = True
    
        except ValueError:
            print("Valor inválido, informe um valor válido")

        except:
            print("Erro")
            
    return resultado


print(f"Resultado {validar_divisao()}")