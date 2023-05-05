from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, tempo=None):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempo

    def get_tempo(self):
        return self.__tempoDeBateria

    def cadastrar(self):
        super().getInformacoes()
        print("Tempo: ",self.__tempoDeBateria)