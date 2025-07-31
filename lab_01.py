
import os

nome_diretorio = "arquivos"

os.mkdir(nome_diretorio)

caminho_diretorio = os.path.abspath(nome_diretorio)


arquivos = {
    "arquivo1.txt": "Linha do arquivo 01",
    "arquivo2.txt": "Linha do arquivo 02",
    "arquivo3.txt": "Linha do arquivo 03"
}

for nome_arquivo, conteudo in arquivos.items():    
    arquivo = open(os.path.join(caminho_diretorio,nome_arquivo),"w")
    arquivo.write(conteudo)
    arquivo.close()
    
for nome_arquivo in os.listdir(caminho_diretorio):
    print(f"Informações do arquivo {nome_arquivo}")
    arquivo = open(os.path.join(caminho_diretorio,nome_arquivo),"r")
    conteudo = arquivo.read()
    print(f"   =>{conteudo}")




