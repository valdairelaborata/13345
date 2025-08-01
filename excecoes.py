
# arquivo = "teste.txt"

# try: 
#     # open(arquivo, "r")
#     a ="10"
#     numero = int(a)    
# except FileNotFoundError:
#     print("Arquivo não encontrado.")
# # except ValueError:
# #     print("Valor informado é inválido!")
# except: 
#     print("Ocorreu um erro.")   
# else:       
#     print("Negação do try")
# finally:
#     print("Fim")

# # a ="Teste"
# # numero = int(a)




# try:
#     arquivo = open("lab_01.txt", "r")
#     arquivo.write("Algum valor")
# except:
#     print("Erro...")

# finally:
#     arquivo.close()


with open("lab_01.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)


print("Fim")