
validos = []
nao_validos = []

def ler_arquivo(arquivo):
    arquivo_ips = open(arquivo, "r")
    lista_ips = arquivo_ips.readlines()
    arquivo_ips.close()
    return lista_ips

def seperar_ips(lista_ips):
    """Aplicar alguma regra para validar se o ip é válido"""
    for index, ip in enumerate(lista_ips):
        if index % 2 == 0:
            validos.append(ip)
        else:
            nao_validos.append(ip)

def escrever_arquivo():
    arquivo_ips_separados = open("ips_separados.txt", "w")

    arquivo_ips_separados.write("[Ips validos]\n")
    for ip in validos:
        arquivo_ips_separados.write(ip)

    arquivo_ips_separados.write("\n")
    arquivo_ips_separados.write("[Ips não validos]\n")
    for ip in nao_validos:
        arquivo_ips_separados.write(ip)    

    arquivo_ips_separados.close()
        

seperar_ips(ler_arquivo("ips.txt"))
escrever_arquivo()

