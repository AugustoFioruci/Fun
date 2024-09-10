class Car:

    def __init__(self, modelo=None, marca=None, cor=None):
        
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.velocidade = 0

    def adicionarCarro(self):

        self.modelo = input(f"Digite o modelo: ")
        self.marca = input(f"Digite o marca: ")
        self.cor = input(f"Digite o cor: ")

    def acelerar(self):

        self.velocidade += 10

    def desacelerar(self):

        self.velocidade -= 10

    def exibir(self):
        print(f"Modelo: {self.modelo} \nMarca: {self.marca}\nCor: {self.cor}\nVelocidade: {self.velocidade}")

listaCarro = []
contagemCarros = 0

while True:
    
    print("Menu:")
    print("1: Adicionar carro")
    print("2: Informações do carro")
    print("3: Acelerar carro")
    print("4: Frear carro")
    print("Sair")

    opcao = int(input("Escolha um numero: "))

    if opcao == 1:
        novoCarro = Car()
        novoCarro.adicionarCarro()
        listaCarro.append(novoCarro)
    elif opcao == 2:
        if not listaCarro:
            print("Nenhum carro cadastrado")
        else:
            print("Lista de carros: ")
            for i, carro in enumerate(listaCarro):
                print(f"{i+1}")
            escolherCarro = int(input(f"Escolha o carro: "))-1
            listaCarro[escolherCarro].exibir()
    elif opcao == 3:
        escolherCarro = int(input(f"Escolha o carro que deseja acelerar: "))-1
        listaCarro[escolherCarro].acelerar()
    elif opcao == 4:
        escolherCarro = int(input(f"Escolha o carro que deseja desacelerar: "))-1
        listaCarro[escolherCarro].desacelerar()
    elif opcao == 5:
        break
    else:
        print("Digite um numero valido!")