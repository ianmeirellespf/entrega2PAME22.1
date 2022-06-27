from funções import *

print("Bem vindo ao sistema do colegio.\nO que você gostaria de fazer?")

pedido=""

while (pedido != "Sair"):
    fazer = input("Que ação você deseja tomar Criar/Listar/Relacionar/Alterar/Deletar/Sair?\n")
    escolha= " "

    if (fazer == "Criar"):
        escolha = input("Digite uma das escolhas Aluno/Professor/Disciplina/Sala:\n")
        if (escolha == "Aluno"):
            funçãocriarAluno()
        elif (escolha == "Professor"):
            funçãocriarProfessor()
        elif (escolha == "Disciplina"):
            funçãocriarDisciplina()
        elif (escolha == "Sala"):
            funçãocriarSala()
        else:
            print("Essa escolha não existe!")
    elif(fazer == "Listar"):
        escolha = input("Digite uma das escolhas Aluno/Professor/Disciplina/Sala:\n")
        if (escolha == "Disciplina"):
            for iddisciplina in dicDisciplinas:
                print(dicDisciplinas[iddisciplina])
        elif (escolha == "Alunos"):
            for idaluno in dicAlunos:
                print(dicAlunos[idaluno])
        elif (escolha == "professores"):
            for idprofessor in dicProfessores:
                print(dicProfessores[idprofessor])
        elif (escolha == "Salas"):
            for idsala in dicSalas:
                print(dicSalas[idsala])
        else:
            print("Essa escolha não existe!")
    elif(fazer == "Relacionar"):
        escolha = input("Digite uma das escolhas Aluno/Professor/Sala:\n")
        if (escolha == "Professor"):
            funçãorelacionarProfessorDisciplina()
        elif (escolha == "Aluno"):
            funçãorelacionarAlunoDisciplina()
        elif (escolha == "Sala"):
            funçãorelacionarSalaDisciplina()
        else:
            print("Essa escolha não existe!")
    elif(fazer == "Alterar"):
        escolha = input("Digite uma das escolhas Aluno/Professor/Disciplina/Sala/alunos :\n")
        if (escolha == "Disciplina"):
            funçãoalterarDisciplina()
        elif (escolha == "Aluno"):#aluno, é no singular, um aluno ali dentro
            funçãoalterarAluno()
        elif (escolha == "Professor"):
            funçãoalterarProfessor()
        elif (escolha == "Sala"):
            funçãoalterarSala()
        elif (escolha == "alunos"):#alunos no plural, significa mudar os alunos de uma disciplina
            funçãoalterarAlunos()
        else:
            print("Essa escolha não existe!")
    elif(fazer == "Deletar"):
        escolha = input("Digite uma das escolhas Aluno/Professor/Disciplina/Sala:\n")
        if (escolha == "Aluno"):
            funçãodeletarAluno()
        elif (escolha == "Professor"):
            funçãodeletarProfessor()
        elif (escolha == "Disciplina"):
            funçãodeletarDisciplina()
        elif (escolha == "Sala"):
            funçãodeletarSala()
        else:
            print("Essa escolha não existe!")
    elif(fazer == "Sair"):
        pedido = fazer
    else:
        print("Essa escolha não existe!")




