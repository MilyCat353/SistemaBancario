#from nome do arqyuvo import nomeda classe
from Conta import Conta

conta1 = Conta(123, "12366-66", "Katrina", 3.0, 1234)
conta2 = Conta(333, "45245-99", "AnaMariaBraga", 50.0, 4231)
print(conta1.extrato())
print(conta2.extrato())
conta1.pix(2, conta2)
print(conta1.extrato())
print(conta2.extrato())