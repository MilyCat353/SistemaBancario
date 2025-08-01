import getpass
import csv
from conta import Conta

# INICIALIZAÇÃO DE VARIÁVEIS
contas = []
agencia = int(input("Digite a agência: "))
numero_conta = int(input("Digite sua conta corrente: "))
senha = getpass.getpass("Digite a senha: ")
contaEncontrada = None
acesso_liberado = False

def lerArquivo():
    with open('contas.csv', newline = '', encoding = 'utf-8', errors = 'ignore') as lerContas:
        leitor = csv.reader(lerContas, delimiter = ',')
        for linha in leitor:
            conta = Conta(int(linha[0]), int(linha[1]),linha[2],float(linha[3]), linha[4])
            contas.append(conta)

def encontrarContaCorrente():
    global contaEncontrada
    for conta in contas:
        if numero_conta == conta.numero:
            contaEncontrada = Conta(conta.agencia, conta.numero, conta.titular, conta.saldo, conta.senha)

def verificarAcesso():
    global contaEncontrada
    global acesso_liberado
    if contaEncontrada == None: # verifica se a conta é Nula (inexistente)
        print("Dados incorretos")
    else:
        # Verificar se o usuário digitou a senha e agência corretamente
        if senha == contaEncontrada.senha and agencia == contaEncontrada.agencia:
            acesso_liberado = True
            print("Acesso liberado")
        else:
            print("Dados incorretos")

def procurarConta(numero):
    for conta in contas:
        if numero == conta.numero:
            return conta 





lerArquivo()
encontrarContaCorrente()
verificarAcesso()

# liberar o acesso ao menu de transações (extrato, pix, etc)

if acesso_liberado ==  True:
    while(True):
        print("1 -  Extrato")
        print("2 -  Saque")
        print("3 -  Deposito")
        print("4 -  Pix")
        transacao = int(input("Escolha a opção desejadan: "))
        if transacao == 1:
            print("O saldo da conta é: ", contaEncontrada.extrato())

        elif transacao == 2:
            valor = float(input("Digite o valor do saque: "))
            if contaEncontrada.sacar(valor):
                print("Sacou com sucesson ainnnnn")
            else:
                print("Saque recusadonn")
        elif transacao == 3:
            valor = float(input("Digite o valor do depósito: "))
            if contaEncontrada.deposito(valor):
                print(f"Depósito de {valor} efetuado com sucesso!")
            else:
                print("Não foi possível realizar o depósito")
        elif transacao == 4:
            valor = float(input("Digite o valor do pix: "))
            conta = int(input("Digite o número da conta que vocẽ deseja transferir: "))
            contaDestino = procurarConta(conta)
            if contaDestino != None:
                conta.contaEncontrada.pix(valor,contaDestino)
                print("Pix realizado com sucesso!")
            else:
                print("Não foi possível encontrar o pix")
        else: 
            print("Opção inválida")
        
