import numpy as np
from molmass import Formula
from mendeleev.vis import periodic_table
from mendeleev import element
from chempy import balance_stoichiometry
from chempy.equilibria import EqSystem

class Calculadora():
    def __init__(self):
        self.escolha=0
        # self.massasMolares = []    

    def menu(self):

        escolha = int(input('[1] - Calcular massa molar\n[2] - Visualizar tabela periódica\n[3] - Acessar os dados de um elemento específico\n[4] - Balancear uma equação\n[5] - Calcular PH\n[6] - Gerar arquivo .txt\n[7] - Encerrar Programa\n=> '))

        while escolha!=7:
            
            match escolha:
                case 1:
                    self.calculaMassaMolar() 
                case 2:
                    self.visualizarTabela()
                case 3:
                    self.dadosElementos()
                case 4:
                    self.balancaEquacao()
                case 5:
                    self.calculaPh()
                case 6:
                    self.geraArquivo()
                case 7:
                    print('Programa Encerrado!')
                    break      
                case _: 
                    print('Comando não reconhecido, por favor tente novamente!\n')   

    def calculaMassaMolar(self):
        formula = input('Digite a fórmula do elemento que você deseja calcular a massa molar: ')
        formula = float(Formula(formula).mass)
        print(f'A massa molar desse elemento é: {formula}\n')
        escolha = int(input('Deseja calcular a massa molar de mais algum elemento?\n[1] - SIM\n[2] - NÃO\n-> '))
        if escolha == 1:
            self.calculaMassaMolar()
        else:
            self.menu()
    
    # def visualizarTabela(self):
    #     periodic_table() 
    #     self.menu()

    def dadosElementos(self):
        elemento = input('Digite o elemento que deseja visualizar as propriedades: ')
        elemento = element(elemento)
        for iso in elemento.isotopes:
            print(f'{iso}')
        escolha = int(input('Deseja visualizar a propriedade de mais algum elemento?\n[1] - SIM\n[2] - NÃO\n-> '))
        if escolha == 1:
            self.dadosElementos()
        else:
            self.menu()

    def balancaEquacao(self):
        reagente = input('Digite o reagente da equação: ').split()
        produto = input('Digite o produto da equação: ').split()
        equacao = balance_stoichiometry(reagente,produto)
        reag, prod = equacao
        print(f'A equação balançeada é: {dict(reag)}{dict(prod)}\n')
        escolha = int(input('Deseja balancear mais alguma equação?\n[1] - SIM\n[2] - NÃO\n-> '))
        if escolha == 1:
            self.balancaEquacao()
        else:
            self.menu()
    
    def calculaPh(self):
        concentracaoElemento = ('Digite a concentração do elemento que você deseja calcular o PH: ')
        concentracaoElemento = -np.log10(concentracaoElemento)
        print('O PH do elemento digitado é: ')
        escolha = int(input('Deseja visualizar o PH de mais algum elemento?\n[1] - SIM\n[2] - NÃO\n-> '))
        if escolha == 1:
            self.calculaPh()
        else:
            self.menu()


start = Calculadora()
start.menu()