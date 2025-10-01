class Ong:
    def __init__(self, cnpj, nome_ong, endereco):
        self.cnpj = cnpj
        self.nome_ong = nome_ong
        self.endereco = endereco

    def __str__(self):
        return f'Ong: {self.nome_ong}\n CNPJ: {self.cnpj}\n Endereço: {self.endereco}'

class Voluntario:
    def __init__(self, cpf, nome_voluntario, idade):
        self.cpf = cpf
        self.nome_voluntario = nome_voluntario
        self.idade = idade

    def __str__(self):
        return f'ID do voluntário(CPF): {self.cpf}\n Nome: {self.nome_voluntario}\n Idade: {self.idade}'
    
class Calculadora:
    def __init__(self):
        '''quantidade de árvores plantadas por porte (inicializam os atributos do objeto. 
        Isso significa que toda calculadora começa com 0 árvores plantadas de cada porte.)'''
        self.plantas_pequenas = 0
        self.plantas_medias = 0
        self.plantas_grandes = 0

    def add_plantas(self, pequeno=0, medio=0, grande=0):
        self.plantas_pequenas += pequeno
        self.plantas_medias += medio
        self.plantas_grandes += grande

    def total_plantas(self):
        return self.plantas_pequenas + self.plantas_medias + self.plantas_grandes

    def exibir_resumo(self):
        return (f"Plantas pequenas: {self.plantas_pequenas}\n"
                f"Plantas médias: {self.plantas_medias}\n"
                f"Plantas grandes: {self.plantas_grandes}\n"
                f"Total de plantas: {self.total_plantas()}")
    
'''cpf1 = input('Digite o número do seu CPF: ')
nome1 = input('Digite seu nome: ')
idade1 = input('Digite sua Idade: ')
voluntario1 = Voluntario(cpf1, nome1, idade1)

print(voluntario1.exibir_voluntario())'''