def tabela(titulo, lista):
    """
    Cria tabela do tipo:
    ================
         titulo
    ================
    1 - lista [0]
    2 - lista [1]
    3 - lista [2]
    4 - lista [3]
    n - lista [n-1]
    ===============
    E se ajusta a len(titulo) ou len(lista[n]):

    :param titulo: recebe titulo para tabela (string)
    :param lista: recebe lista de strings para criar opções
    :return: none
    """
    maior = ''

    for c in lista:
        caixa = len(c)
        if caixa > len(maior):
            maior = c
        if titulo > maior:
            maior = titulo

    tamanho = int(len(maior) + 8)
    laterais = (len(maior) - len(titulo) + 8)//2

    print('='*tamanho)
    print(' '*laterais + f'{titulo}' + ' '*laterais)
    print('='*tamanho)
    print('0 - Encerra')
    for cont, funcao in enumerate(lista):
        print(f'{cont+1} - {funcao}')
    print('='*tamanho)

def tabela_premium(caminho, linhas, colunas):
    import csv
    contador = 0 

    with open(caminho, 'r') as arquivo:
        leitor = csv.reader(arquivo)

        for leitura in leitor:
            for linha in linhas:
                if contador == int(linha):
                    print(leitura)
            contador+=1

tabela_premium('teste.csv', [2, 0], [2])