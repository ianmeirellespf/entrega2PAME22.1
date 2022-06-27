from classes import *

dicAlunos={} #todos os alunos
dicProfessores={} #todos os professores
dicSalas={} #todas as salas
dicDisciplinas={} #todas as discplinas

#criando
def funçãocriarAluno():
    nome = input("Digite  o nome do Aluno: ")
    idade = input("Digite a idade do Aluno: ")
    dre = input("Digite o DRE do aluno: ")
    pedido = " "
    idaluno = 0
    while (pedido != "aceito"):
        idaluno += 1
        pedido = dicAlunos.get(idaluno,"aceito")
    dicAlunos[idaluno] = aluno(nome, idade,dre )
    print("ID do aluno: "+str(idaluno))

def funçãocriarProfessor():
    nome = input("Digite  o nome do professor: ")
    idade = input("Digite a idade do professor: ")
    dre = input("Digite o DRE do professor: ")
    pedido = " "
    idprofessor = 0
    while (pedido != "aceito"):
        idprofessor += 1
        pedido = dicProfessores.get(idprofessor,"aceito")
    dicProfessores[idprofessor] = professor(nome, idade,dre )
    print("ID do professor: "+str(idprofessor))

def funçãocriarDisciplina():
    nomedisciplina = input("Digite o nome da disciplina: ")
    horariocomeça  = input("Digite a hora que começa a  disciplina: ")
    horarioacaba   = input("Digite a hora que acaba a  disciplina: ")
    pedido = " "
    iddisciplina = 0
    while (pedido != "aceito"):
        iddisciplina += 1
        pedido = dicAlunos.get(iddisciplina,"aceito")
    dicDisciplinas[iddisciplina] = disciplina(nomedisciplina,horariocomeça,horarioacaba)
    print("ID da disciplina: "+str(iddisciplina))

def funçãocriarSala():
    numero = input("Digite a placa do ônibus: ")
    andar= input("Digite o modelo do ônibus: ")
    capacidademax = input("Digite a capacidade maxima da sala: ")
    horarioabre=input("Digite a capacidade maxima da sala: ")
    horariofecha=input("Digite a capacidade maxima da sala: ")
    pedido = " "
    idsala = 0
    while (pedido != "aceito"):
        idsala += 1
        pedido = dicAlunos.get(idsala,"aceito")
    dicSalas[idsala] = sala(numero,andar, capacidademax,horarioabre,horariofecha)
    print("ID da sala: "+str(idsala))

#associar
def funçãorelacionarProfessorDisciplina():
    idprofessor = input("Digite o ID do professor: ")
    iddisciplina = input("Digite o ID da disciplina: ")
    professor = dicProfessores[idprofessor]
    disciplina = dicDisciplinas[iddisciplina]
    dicProfessores[iddisciplina] = disciplina.mudarProfessor(professor)
    dicDisciplinas[iddisciplina] = disciplina

def funçãorelacionarAlunoDisciplina():
    idaluno = input("Digite o ID do aluno: ")
    iddisciplina = input("Digite o ID da disciplina : ")
    aluno = dicAlunos[idaluno]
    disciplina = dicDisciplinas[iddisciplina]
    disciplina.adicionarAluno(idaluno, aluno)
    dicDisciplinas[iddisciplina] = disciplina

def funçãorelacionarSalaDisciplina():
    idsala = input("Digite o ID da sala: ")
    iddisciplina = input("Digite o ID da disciplina: ")
    sala = dicSalas[idsala]
    disciplina = dicDisciplinas[iddisciplina]
    dicSalas[iddisciplina] = disciplina.mudarsala(sala)
    dicDisciplinas[iddisciplina] = disciplina

#excluir

def funçãodeletarAluno():
    idaluno = int(input("Digite o ID do Aluno: "))
    dicAlunos.pop(idaluno) 

def funçãodeletarProfessor():#no sim, vc tira a ocupação do professor. pra excluir ele, precisa tirar a ocupação e depois repetir e mandar "Nao"
    resposta = input("Você deseja alterar um professor ja alocado? ")
    if (resposta == "Sim"):
        iddisciplina = int(input("Digite o id da disciplina: "))
        disciplina = dicDisciplinas[iddisciplina]
        disciplina.professor = " "
        
    elif (resposta == "Nao"):
        idprofessor = int(input("Digite o ID do professor: "))
        dicProfessores.pop(idprofessor)

def funçãodeletarDisciplina():
    iddisciplina = int(input("Digite o ID da disciplina: "))
    disciplina = dicDisciplinas[iddisciplina]
    for aluno in disciplina.alunos:
        pedido = " "
        idaluno = 0
        while (pedido != "ID disponível!"):
            idaluno += 1
            pedido = dicAlunos.get(idaluno, "ID disponível!")
        dicAlunos[idaluno] = aluno

    if (disciplina.professor != " "):
        pedido = " "
        idprofessor = 0
        while (pedido != "ID disponível!"):
            idprofessor += 1
            pedido = dicProfessores.get(idprofessor, "ID disponível!")
        dicProfessores[idprofessor] = disciplina.professor

    if (disciplina.sala != " "):
        pedido = " "
        idsala = 0
        while (pedido != "ID disponível!"):
            idsala += 1
            pedido = dicSalas.get(idsala, "ID disponível!")
        dicSalas[idsala] = disciplina.sala

def funçãodeletarSala(): #no sim, vc tira a ocupação da sala. pra excluir ela, precisa tirar a ocupação e depois repetir e mandar "Nao"
    resposta = input("Você deseja alterar uma sala ja ocupada? ")
    if (resposta == "Sim"):
        iddisciplina = int(input("Digite o id da disciplina: "))
        disciplina = dicDisciplinas[iddisciplina]
        disciplina.sala = " "
        
    elif (resposta == "Nao"):
        idsala = int(input("Digite o ID da sala: "))
        dicSalas.pop(idsala)

#alterando

def funçãoalterarDisciplina():
    iddisciplina = int(input("Digite o ID da disciplina: "))
    disciplina = dicDisciplinas[iddisciplina]
    disciplina.alterarDisciplinha()

def funçãoalterarAluno():
    idaluno = int(input("Digite o ID do aluno: "))
    aluno = dicAlunos[idaluno]
    dicAlunos[idaluno] = aluno.alterarAluno()

def funçãoalterarProfessor():
    resposta = input("Você deseja alterar um professor ja alocado? ")
    if (resposta == "Sim"):
        iddisciplina = int(input("Digite o ID da disciplina: "))
        disciplina = dicDisciplinas[iddisciplina]
        disciplina.professor = disciplina.professor.alterarProfessor()
        dicDisciplinas[iddisciplina] = disciplina
    elif (resposta == "Nao"):
        idprofessor = input("Digite o ID do professor: ")
        professor = dicProfessores[idprofessor]
        dicProfessores[idprofessor] = professor.alterarProfessor()
    else:
        print("Não foi feita alteração.")

def funçãoalterarSala():
    resposta = input("Você deseja alterar uma sala  ja reservada? ")
    if (resposta == "Sim"):
        iddisciplina = int(input("Digite o ID da disciplina: "))
        disciplina = dicDisciplinas[iddisciplina]
        disciplina.sala = disciplina.sala.alterarSala()
        dicDisciplinas[iddisciplina] = disciplina
    elif (resposta == "Nao"):
        idsala = input("Digite o ID da sala: ")
        sala = dicProfessores[idsala]
        dicSalas[idsala] = sala.alterarSala()
    else:
        print("Não foi feita alteração.")

def funçãoalterarAlunos():
    iddisiplina = int(input("Digite o ID da disciplina com os alunos que deseja alterar: "))
    disciplina = dicDisciplinas[iddisiplina]
    for aluno in disciplina.alunos:
        print(aluno)
        resposta = input("Deseja Alterar,Remover ou Manter esse aluno? ")
        if (resposta == "Alterar"):
            pedido = " "
            idaluno = 0
            while (pedido != "ID disponível!"):
                idaluno += 1
                pedido = dicAlunos.get(idaluno, "ID disponível!")
            dicAlunos[idaluno] = disciplina.alunos.pop(aluno)
            idaluno = int(input("Digite o ID do aluno que deseja usar: "))
            disciplina.adicionarAluno(idaluno, dicAlunos.pop(idaluno))
            print("ID do aluno :"+str(idaluno))
        elif (resposta == "Remover"):
            pedido = " "
            idaluno = 0
            while (pedido != "ID disponível!"):
                idaluno += 1
                pedido = dicAlunos.get(idaluno, "ID disponível!")
            dicAlunos[idaluno] = disciplina.alunos.pop(aluno)
            print("ID do aluno:"+str(idaluno))
        elif (resposta == "Manter"):
            pass


    dicDisciplinas[idaluno] = disciplina

