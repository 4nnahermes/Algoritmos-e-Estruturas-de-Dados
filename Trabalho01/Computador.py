from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo=None, cor=None, preco=None):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preço: ", self.preco)

    @abstractmethod
    def cadastrar(self):
        print("Produto Cadastrado")