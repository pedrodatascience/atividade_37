import classes as cl

if __name__ == '__main__':
    #entrada de dados
    nome = input('Informe o nome do usuário: ')
    email = input('Informe o e-mail do usuário: ')
    cpf = input('Informe o cpf do usuário: ')
    profissao = input('Informe a profissao do usuário: ')
    endereco = input('Informe o endereco do usuário: ')
    telefone = input('Informe o telefone do usuário: ')

    #instancia a classe pessoa física
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone)

    #entrada de dados
    nome_fantasia = input('Informe o nome da empresa: ')
    email = input('Informe o e-mail da empresa: ')
    cnpj = input('Informe o cnpj da empresa: ')
    razao_social = input('Informe a razao social da empresa: ')
    endereco = input('Informe o endereco da empresa: ')
    telefone = input('Informe o telefone da empresa: ')

    #instancia a classe pessoa jurídica
    empresa = cl.PessoaJuridica(nome_fantasia, razao_social, cnpj, endereco, email, telefone)
    

    #saída de dados
    usuario.mostrar_cartao_visitas()
    print('-'*30)
    empresa.mostrar_cartao_visitas()