from controle import Controle

controle = Controle()

def menu():
    while True:
        print("\n--- Sistema de Reflorestamento Urbano ---")
        print("1 - Cadastrar ONG")
        print("2 - Listar ONGs")
        print("3 - Atualizar ONG")
        print("4 - Deletar ONG")
        print("5 - Cadastrar Voluntário")
        print("6 - Listar Voluntários")
        print("7 - Atualizar Voluntário")
        print("8 - Deletar Voluntário")
        print("9 - Registrar Plantio")
        print("10 - Ver Resumo do Plantio")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cnpj = input("CNPJ da ONG: ")
            nome_ong = input("Nome da ONG: ")
            endereco = input("Endereço da ONG: ")
            controle.criar_ong(cnpj, nome_ong, endereco)
            print("ONG cadastrada com sucesso!")

        elif escolha == "2":
            for ong in controle.listar_ongs():
                print(ong)

        elif escolha == "3":
            cnpj = input("CNPJ da ONG a atualizar: ")
            nome_ong = input("Novo nome (ou enter para manter): ")
            endereco = input("Novo endereço (ou enter para manter): ")
            if controle.atualizar_ong(cnpj, nome_ong or None, endereco or None):
                print("ONG atualizada!")
            else:
                print("ONG não encontrada.")

        elif escolha == "4":
            cnpj = input("CNPJ da ONG a deletar: ")
            if controle.deletar_ong(cnpj):
                print("ONG deletada!")
            else:
                print("ONG não encontrada.")

        elif escolha == "5":
            cpf = input("CPF do voluntário: ")
            nome_voluntario = input("Nome do voluntário: ")
            idade = int(input("Idade do voluntário: "))
            controle.criar_voluntario(cpf, nome_voluntario, idade)
            print("Voluntário cadastrado com sucesso!")

        elif escolha == "6":
            for vol in controle.listar_voluntarios():
                print(vol)

        elif escolha == "7":
            cpf = input("CPF do voluntário a atualizar: ")
            nome_voluntario = input("Novo nome (ou enter para manter): ")
            idade_input = input("Nova idade (ou enter para manter): ")
            idade = int(idade_input) if idade_input else None
            if controle.atualizar_voluntario(cpf, nome_voluntario or None, idade):
                print("Voluntário atualizado!")
            else:
                print("Voluntário não encontrado.")

        elif escolha == "8":
            cpf = input("CPF do voluntário a deletar: ")
            if controle.deletar_voluntario(cpf):
                print("Voluntário deletado!")
            else:
                print("Voluntário não encontrado.")

        elif escolha == "9":
            pequeno = int(input("Quantidade de plantas pequenas: "))
            medio = int(input("Quantidade de plantas médias: "))
            grande = int(input("Quantidade de plantas grandes: "))
            controle.calculadora.add_plantas(pequeno, medio, grande)
            print("Plantio registrado!")

        elif escolha == "10":
            print(controle.calculadora.exibir_resumo())

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()