# Biblioteca para trabalhar com Frações
from fractions import Fraction 
# Biblioteca para usar funcoes do sistema operacional
import os

# Função para limpar o terminal
def limpaTerminal():
	os.system("cls" if os.name == "nt" else "clear")

# Função para calcular o Limite Rapido
def limiteRapido(somaPonderada):
        if somaPonderada <= 0:
                return -1
        else:
                return 1

# Função Rampa
def funcaoRampa(somaPonderada):
	if somaPonderada < 0:
		return 0
	elif somaPonderada <= 0 and somaPonderada <= 1:
		return somaPonderada
	else:
		return 1

# Funçãoo Sigmoide
def funcaoSigmoide(somaPonderada):
	if somaPonderada >= 0:
		# return 1 - 1/(1+somaPonderada)
		f = 1 - Fraction(1,(1+somaPonderada))
		return f
	else:
		# return -1 + 1/(1-somaPonderada)
		f = -1 + Fraction(1,(1-somaPonderada))
		return f

#Função para imprir os dados
def imprimeResultados(somaPonderada):
	limpaTerminal()
	funcao = input("\nQual funcao voce deseja calcular? \n 1 - Limite Rapida\n 2 - Funcao Rampa \n 3 - Funcao Sigmoide \n 4 - Todas\n >>> ")

	if funcao == '1':
		print("\nLimite Rapido = ", limiteRapido(somaPonderada))

	elif funcao == '2':
		print("\nFuncao Rampa = ", funcaoRampa(somaPonderada))
	
	elif funcao == '3':
		print("\nFuncao Sigmoide = ", funcaoSigmoide(somaPonderada))
	
	elif funcao == '4':
		print("\nLimite Rapido = ", limiteRapido(somaPonderada))
		print("Funcao Rampa = ", funcaoRampa(somaPonderada))
		print("Funcao Sigmoide = ", funcaoSigmoide(somaPonderada))
	
	else:
		print("\nOpcao invalida")


# MAIN	
somaPonderada = 0

# Do While simulado, para receber multiplas entradas
while True:
	entrada = input("Informe o valor de entrada: ")
	peso = input("Informe o peso: ")
 
	# calculo da soma ponderada
	somaPonderada += int(entrada) * int(peso)

	aux = input("Adicionar mais entradas? (s/n)")
	limpaTerminal()
	if aux != 's':
		break
 
imprimeResultados(somaPonderada)