import getpass
import csv
from conta import Conta

#Inicialização de variaveis

contas = []

acesso_liberado = False
contaEncontrada = None

agencia = int(input("Digite a agẽncia: "))
numero_conta = int(input("Digite sua conta corente: "))
senha = getpass.getpass("Digite a semha: ")

def lerArquivo():
    with open('contas.csv', newline = '', encoding = 'utf-8', errors = 'ignore') as lerContas:
        leitor = csv.reader(lerContas, delimiter = ',')
        for linha in leitor:
            conta = Conta(int(linha[0]), int(linha[1]), linha[2], float(linha[3]), linha[4])
            contas.append(conta)

def encontrarContaCorrente():

    global contaEncontrada
    for conta in contas:
        if numero_conta == conta.numero:
            contaEncontrada = Conta(conta.agencia, conta.numero, conta.titular, conta.saldo, conta.senha)

def verificarAcesso():
    global contaEncontrada
    if contaEncontrada == None:
        print("Dados incorretos")
        print("Dacos incorretos")
    else:
        print(contaEncontrada.senha)
        if senha == contaEncontrada.senha and agencia == contaEncontrada.agencia:
            print("Acesso liberado")
        else:
            print("Dados incorretos")


lerArquivo()
encontrarContaCorrente()
verificarAcesso()
