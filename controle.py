from modelo import Ong, Voluntario, Calculadora

class Controle:
    def __init__(self):
        self.ongs = []
        self.voluntarios = []
        self.calculadora = Calculadora()

    # CRUD ONG
    def criar_ong(self, cnpj, nome_ong, endereco):
        ong = Ong(cnpj, nome_ong, endereco)
        self.ongs.append(ong)

    def listar_ongs(self):
        return self.ongs

    def atualizar_ong(self, cnpj, novo_nome_ong=None, novo_endereco=None):
        for ong in self.ongs:
            if ong.cnpj == cnpj:
                if novo_nome_ong:
                    ong.nome_ong = novo_nome_ong
                if novo_endereco:
                    ong.endereco = novo_endereco
                return True
        return False

    def deletar_ong(self, cnpj):
        for ong in self.ongs:
            if ong.cnpj == cnpj:
                self.ongs.remove(ong)
                return True
        return False

    # CRUD Voluntário
    def criar_voluntario(self, cpf, nome_voluntario, idade):
        voluntario = Voluntario(cpf, nome_voluntario, idade)
        self.voluntarios.append(voluntario)

    def listar_voluntarios(self):
        return self.voluntarios

    def atualizar_voluntario(self, cpf, novo_nome_voluntario=None, nova_idade=None):
        for vol in self.voluntarios:
            if vol.cpf == cpf:
                if novo_nome_voluntario:
                    vol.nome_voluntario = novo_nome_voluntario
                if nova_idade:
                    vol.idade = nova_idade
                return True
        return False

    def deletar_voluntario(self, cpf):
        for vol in self.voluntarios:
            if vol.cpf == cpf:
                self.voluntarios.remove(vol)
                return True
        return False