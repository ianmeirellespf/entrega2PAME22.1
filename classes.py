class pessoa:
    def __init__ (self,nome,idade,dre):
        self.nome= nome
        self.idade= idade
        self.dre= dre
    def __str__(self):
        return f"Nome: { self.nome }\ idade: { self.idade }\ DRE { self.dre }"

class professor(pessoa):
    

    def alterarProfessor(self):
        self.nome = input("Digite o nome do professor: ")
        self.idade = input("Digite a idade professor: ")
        self.dre = input("Digite o DRE do professor: ")
        
        return self   
    def __str__(self):
        return f"Nome: { self.nome }\ idade: { self.idade }\ DRE { self.dre }"

class aluno(pessoa):

    def alterarAluno(self):
     
        self.nome = input("Digite o nome do aluno: ")
        self.idade = input("Digite a idade do aluno: ")
        self.dre = input("Digite o DRE do aluno: ")
        return self
    


class sala():
    def __init__ (self,numero,andar,capacidademax,horarioabre,horariofecha):
        self.numero= numero
        self.andar = andar
        self.capacidademax= capacidademax
        self.horarioabre = horarioabre
        self.horariofecha = horariofecha
    def alterarSala(self):
     
        self.numero = input("Digite o numero da sala: ")
        self.andar = input("Digite o andar da sala: ")
        self.capacidademax = input("Digite a capacidade maxima da sala: ")
        self.horarioabre = input("Digite o horario que abre a sala: ")
        self.horariofecha = input("Digite o horario que fecha a sala: ")

        return self
    def __str__(self):
        return f"numero: { self.numero }\ andar : { self.andar}\ capacidade maxima { self.capacidademax} \ horario de funcionamento { self.horarioabre}-{ self.horariofecha}  "

class disciplina:
    def __init__ (self,nomedisciplina,horariocomeça,horarioacaba):
        self.nomedisciplina= nomedisciplina
        self.professor= ""
        self.alunos=[]
        self.sala= ""
        self.horariocomeça=horariocomeça
        self.horarioacaba=horarioacaba
    def __str__(self):
      return f"nome: { self.nomedisciplina }\ horario :{self.horariocomeça} - {self.horarioacaba}"
    
    def alterarDisciplinha(self):
     
        self.nomedisciplina= input("Digite o numero da disciplina: ")
        self.horariocomeça = input("Digite a hora que começa a disciplina: ")
        self.horarioacaba = input("Digite a hora que acaba a disciplina: ")
        

        return self
 
    def mudarProfessor(self,professor):
        print("O professor foi removido da disciplina!")
        professorRemovido = self.professor
        self.professor=professor
        print("O novo professor foi colocado na disciplina")
        return professorRemovido

    def mudarSala(self,sala):
        print("A sala foi removida da disciplina")
        salaRemovida = self.sala
        self.sala=sala
        print("A nova sala foi associada a disciplina")
        return salaRemovida

    def adicionarAluno(self, idaluno, aluno):
        self.alunos.insert(idaluno, aluno)




    
    