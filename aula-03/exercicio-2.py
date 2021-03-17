from fractions import Fraction 
import os


def limpaTerminal():
	os.system("cls" if os.name == "nt" else "clear")

def limiteRapido(s):
        if s <= 0:
                return -1
        else:
                return 1

def funcaoRampa(s):
	if s < 0:
		return 0
	elif s <= 0 and s <= 1:
		return s
	else:
		return 1

def funcaoSigmoide(s):
	if s >= 0:
		# return 1 - 1/(1+s)
		f = 1 - Fraction(1,(1+s))
		return f
	else:
		# return -1 + 1/(1-s)
		f = -1 + Fraction(1,(1-s))
		return f

s = 0
while True:
	entrada = input("Informe o valor de entrada: ")
	peso = input("Informe o peso: ")
 
	s += int(entrada) * int(peso)

	aux = input("Adicionar mais entradas? (s/n)")
	limpaTerminal()
	if aux != 's':
		break

limpaTerminal()
funcao = input("\nQual funcao voce deseja calcular? \n 1 - Limite Rapida\n 2 - Funcao Rampa \n 3 - Funcao Sigmoide \n 4 - Todas\n >>> ")

limpaTerminal()
if funcao == '1':
    print("\nLimite Rapido = ", limiteRapido(s))
elif funcao == '2':
    print("\nFuncao Rampa = ", funcaoRampa(s))
elif funcao == '3':
    print("\nFuncao Sigmoide = ", funcaoSigmoide(s))
elif funcao == '4':
    print("\nLimite Rapido = ", limiteRapido(s))
    print("Funcao Rampa = ", funcaoRampa(s))
    print("Funcao Sigmoide = ", funcaoSigmoide(s))
else:
    print("\nOpcao invalida")
