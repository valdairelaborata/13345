usuario = input("Informa o usuário:")
senha = input("Informe a senha:")

while usuario == senha:
    print("Usuário e senha não pode ser igual! Infome novamente.")
    usuario = input("Informa o usuário:")
    senha = input("Informe a senha:")

print("Usuário e senha ok!")