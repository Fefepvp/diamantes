def Erro_Int(msg):
    '''
    Cria um laço que trata erros e só deixa passar números inteiros.
    :param msg: Frase para input
    :return: num tratado
    '''
    while True:    
        num = input(msg)
        try:
            int(num)
            return int(num)
        except TypeError:
            print("Por favor digite um número inteiro!")
        except ValueError:
            print("Por favor digite um número inteiro!")
