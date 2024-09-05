import csv

with open('diamonds.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    contador = 0
    for linha in leitor:
        print(linha[2], end='')
        print(linha[3])
        contador += 1
        if contador ==3:
            break
