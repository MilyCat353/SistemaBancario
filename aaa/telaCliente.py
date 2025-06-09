import getpass
import csv
from conta import Conta
contas = []
with open('contas.csv', newline = '', encoding = 'utf-8', errors = 'ignore') as lerContas:
    leitor = csv.reader(lerContas, delimiter = ',')
    for linha in leitor:
        conta = Conta(linha[0], linha[1], linha[2], linha[3], linha[4])
        contas.append(conta)
print (contas)

agencia = int(input("Digite a agẽncia: "))
numero_conta = int(input("Digite sua conta corente: "))
senha = getpass.getpass("Digite a semha: ")
