from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, potencia=None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potencia

    def cadastrar(self):
        super().getInformacoes()
        print("Potência da Fonte: ", self._potenciaDaFonte)