
relatorios = []

while True:
    nome = input("Informe o nome do aluno:")
    if nome == "":
        break
   
    notas = []
    soma = 0

    for nota in range(3):
        nota_informada = float(input(f"Informe a nota {nota + 1} para o aluno {nome}:"))
        notas.append(nota_informada)
        soma =  soma + nota_informada

    relatorio = f"O(A) aluno(a): {nome} - teve as notas {notas}, com média de: {soma / 3} "
    relatorios.append(relatorio)


for relatorio_aluno in relatorios:
    print(relatorio_aluno)
    