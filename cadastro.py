infoCadastro = {'Nome': '', 'Sobrenome': '', 'Idade': '', 'Gmail': '', 'Senha': ''}
validação = False
gmail = ''
senha = ''

def validName(infoCadastro):
    if infoCadastro['Nome'].isalpha() and infoCadastro['Sobrenome'].isalpha():
        return True
    else:
        return False
    
def validGmail(gmail):
    gmail.lower()
    posição = gmail[-10:] 

    if posição == '@gmail.com':
        return True
    else:
        return False    


def validSenha(infoCadastro, senha):
    infoCadastro['Senha'].lower() 

    if len(infoCadastro['Senha']) < 6:
        return False
    elif infoCadastro['Senha'] != senha.lower():
        return False
    else:
        return True

def cadastro(infoCadastro):

    print("\nInsira suas informações abaixo para a realização do seu cadastro.")

    infoCadastro['Nome'] = input("Nome: ")
    infoCadastro['Sobrenome'] = input("Ultimo Sobrenome: ")
    validação = validName(infoCadastro)

    if not validação:
        print ('\nO nome fornecido contém caracteres invalidos. Cadastro encerrado.')
        return

    infoCadastro['Idade'] = int(input('Idade: '))
    
    if infoCadastro['Idade'] < 18:
        print('\nVoce não tem idade suficiente. Cadastro encerrado.')
        return

    gmail = input('Gmail: ')
    validação = validGmail(gmail)

    if not validação:
        print('\nGmail invalido. Cadastro encerrado.')
        return
    else:
        infoCadastro['Gmail'] = gmail



    infoCadastro['Senha'] = input('Senha (minimo 6 caracteres): ')
    senha = input('Digite sua senha novamente: ')
    validação = validSenha(infoCadastro, senha)

    if not validação:
        print('\nSenhas não são iguais ou valor minimo não atingido. Cadastro encerrado.')
        return

    print('\nCadastro finalizado com sucesso!')


cadastro(infoCadastro)

