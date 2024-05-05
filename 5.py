alunos_lista = []

alunos_set = set()

def adicionar_aluno(nome):
    alunos_lista.append(nome)
    alunos_set.add(nome)
    print(f"Aluno {nome} adicionado com sucesso!")

def remover_aluno(nome):
    if nome in alunos_lista:
        alunos_lista.remove(nome)
        alunos_set.remove(nome)
        print(f"Aluno {nome} removido.")
    else:
        print(f"Aluno {nome} não encontrado.")

def verificar_aluno(nome):
    if nome in alunos_lista:
        print(f"Aluno {nome} está na lista.")
    else:
        print(f"Aluno {nome} não está na lista.")

adicionar_aluno("João")
adicionar_aluno("Maria")
adicionar_aluno("Carlos")

verificar_aluno("Maria")
verificar_aluno("Pedro")

remover_aluno("Carlos")

verificar_aluno("Carlos")