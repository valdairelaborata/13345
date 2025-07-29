

# def numero():
#     x = 10
#     print("Valor dentro da função: {}".format(x))

# x = 20 


# print("Valor fora da função: {}".format(x))

# numero()


# def soma(*args):
#     return sum(args)


# resultado = soma(1, 6, 8, 10, 41)

# print(resultado)

def lista_de_compras(** kwargs):
    print(kwargs)


lista_de_compras(hortifruti=6, padaria=10, acougue=2)