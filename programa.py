from funcoes import *
from tabulate import tabulate

alunos = []  


def menu():
    print(" GERENCIADOR DE NOTAS ")
    print("1 - Cadastrar aluno e notas")
    print("2 - Exibir relatório")
    print("0 - Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("nEncerrando o programa... Até logo! ")
        break

    elif opcao == '1':
        nome = input("Digite o nome do aluno: ")

        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Por favor, insira um número válido.")

        media = calcular_media(notas)
        situacao = verificar_situacao(media)

        alunos.append({
            "Nome": nome,
            "Notas": notas,
            "Média": round(media, 2),
            "Situação": situacao
        })

        print(f"nAluno {nome} cadastrado com sucesso!")

    elif opcao == '2':
        if not alunos:
            print("\nNenhum aluno cadastrado ainda.")
        else:
            tabela = []
            for a in alunos:
                notas_str = ", ".join(map(str, a["Notas"]))
                tabela.append([a["Nome"], notas_str, a["Média"], a["Situação"]])

            print(" RELATÓRIO DE ALUNOS ")
            print(tabulate(
                tabela,
                headers=["Nome", "Notas", "Média", "Situação"],
                tablefmt="fancy_grid"
            ))

    else:
        print("Opção inválida! Tente novamente.")
