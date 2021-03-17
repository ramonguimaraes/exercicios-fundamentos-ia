# Biblioteca para trabalhar com Frações
from fractions import Fraction 

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
		f = 1 - Fraction(1,(1+somaPonderada))
		return f
	else:
		f = -1 + Fraction(1,(1-somaPonderada))
		return f


#Função para imprir os dados
def imprimeInformacoes(somaPonderada):
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



#MAIN

# Entrada de dados
entrada = input("Informe o valor de entrada: ")
peso = input("Informe o peso: ")

#Calculando a soma ponderada
somaPonderada = int(entrada) * int(peso)

imprimeInformacoes(somaPonderada)