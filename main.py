import csv
from estetica import tabela
from tratamento import Erro_Int

lista =[]
lista_caracteristicas = []
while True:
    
    tabela('analise de diamantes', ['Geral'])
    
    num = Erro_Int('Digite sua opção de analise: ')
    
    if num == 0:
        break
    
    if num == 1:
        while True:
            identificador = Erro_Int('Digite o numero de identificação do diamante, 0 encerra: ')
            if identificador == 0:
                break
            else:    
                lista.append(identificador)
                
        tabela('características', ['Carat', 'Cut', 'Color', 'Clarity', 'Depth', 'table', 'Price', 'Lenght', 'Widgth'])
        
        while True:
            caracteristicas = Erro_Int('Digite as características a serem analisadas: ')
            if caracteristicas == 0:
                break
            elif caracteristicas in lista_caracteristicas:
                print('Já escolheu essa característica!')
            else:
                lista_caracteristicas.append(caracteristicas)


        for contador in lista:
            pulador = 0
            with open('diamonds.csv', 'r') as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    if pulador != 0:
                        if int(linha[0]) == contador:
                            print(linha)
                            break
                    pulador +=1
        #cabeçalho

        print('='*20)
        for caracteristica in lista_caracteristicas:
            print(f'')
                        
