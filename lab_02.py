quantidade_turmas = int(input("Informe o quantidde de turmas:"))
turmas_com_alunos_informados = 0
total_alunos = 0

quantidade_alunos = 0

while turmas_com_alunos_informados < quantidade_turmas:
    turmas_com_alunos_informados = turmas_com_alunos_informados + 1
    quantidade_alunos = int(input(f"Informe a quantidade de alunos para a turma {turmas_com_alunos_informados}:"))    

    while quantidade_alunos > 40:
        print("A quantidade de alunos não pode ser superior a 40!")
        quantidade_alunos = int(input(f"Informe novamente a quantidade de alunos para a turma {turmas_com_alunos_informados}:"))    

    total_alunos = total_alunos + quantidade_alunos


print(f"Foram informados {total_alunos} alunos para {quantidade_turmas} turmas.")
print(f"A média por turma foi de {total_alunos / quantidade_turmas}")
