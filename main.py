from molmass import Formula

class Calculadora():
    def __init__(self):
        self.escolha=0

    def menu(self):
        escolha = int(input('[1] - Calcular massa molar\n[2] - Visualizar tabela periódica\n[3] - Acessar os dados de um elemento específico\n[4] - Balancear uma equação\n[5] - Cinética Química\n[6] - Calcular PH\n=>'))

        while escolha!=7:
            
            match escolha:
                case 1:
                    self.cadastrarAcao() 
                case 2:
                    self.cadastrarAcionista()
                case 3:
                    self.cadastraTransacao()
                case 4:
                    self.validaTransacao()
                case 5:
                    self.listarAcoes()
                case 6:
                    self.gerarArquivo()
                case 7:
                    print('Programa encerrado!')
                    break                  
                case _: 
                    print('Comando não reconhecido, por favor tente novamente!\n')   