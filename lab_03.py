
# pessoas = {"nome": "Nome da pessoa", "idade": 25, "cidade": "Curitiba"}

# dados_pessoa = f"Nome: {pessoas['nome']} e tem {pessoas['idade']} anos de idade"

# print(dados_pessoa)



pessoas = {"nome": "Nome da pessoa", "idade": 25, "cidade": "Curitiba",
           "contatos": {
               "residencial": 888888888, "comercial": 99999999999
               }
               }

dados_pessoa = f"Nome: {pessoas['nome']} e tem {pessoas['idade']} anos de idade. O Contato residencial é: {pessoas["contatos"]["residencial"]}"

print(dados_pessoa)