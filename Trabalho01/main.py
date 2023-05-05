from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop("Vostro Small","Preto",5.199,"180W")
print(d1.modelo,"|",d1.cor,"|",d1.preco,"|",d1._potenciaDaFonte)

n1 = Notebook("Inspiron 15 3000","Cinza",5.448,"6 horas")
print(n1.modelo,"|",n1.cor,"|",n1.preco,"|",n1.get_tempo())
