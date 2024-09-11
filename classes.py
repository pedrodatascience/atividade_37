#NOTE: superclasse, classe-pai, classe-base
class Pessoa:
    #atributos
    def __init__(self, endereco, email, telefone):
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        

    #método
    def mostrar_cartao_visitas(self):
        print(f'Endereço: {self.endereco}.')
        print(f'E-mail: {self.email}.')
        print(f'Telefone: {self.telefone}.')

    # NOTE: subclasse, classe-filha, classe derivada Pessoa Física
class PessoaFisica(Pessoa):
    #polimorfismo do construtor
    def __init__(self,nome, cpf, profissao, endereco, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        super().__init__(endereco, email, telefone)

    def mostrar_cartao_visitas(self):
        print(f'Nome do usuário: {self.nome}.')
        print(f'CPF do usuário: {self.cpf}.')
        print(f'Profissão do usuário: {self.profissao}.')
        super().mostrar_cartao_visitas()

#nova classe
class PessoaJuridica(Pessoa):
    # poliformismo do construtor
    def __int__(self, nome_fantasia, razao_social, cnpj, endereco, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        super().__init__(endereco, email, telefone)

    def mostrar_cartao_visitas(self):
        print(f'Nome da empresa: {self.nome_fantasia}.')
        print(f'Razão social: {self.razao_social}.')
        print(f'CNPJ: {self.cnpj}.')
        super().mostrar_cartao_visitas()