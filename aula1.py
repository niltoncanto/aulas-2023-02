
class Automovel:
    # Atributos da classe Automovel
    # construtor da classe
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Criando objetos da classe Automovel
auto1 = Automovel("Ford", "Fiesta", 2019)
auto2 = Automovel("Fiat", "Palio", 2018)


""" # Atributos do objeto auto1
auto1.marca = "Ford"
auto1.modelo = "Fiesta"
auto1.ano = 2019
# Atributos do objeto auto2
auto2.marca = "Fiat"
auto2.modelo = "Palio"
auto2.ano = 2018 """

# Imprimindo os atributos dos objetos
print(auto1.marca, auto1.modelo, auto1.ano)
print(auto2.marca, auto2.modelo, auto2.ano)
print("fim do programa")

def soma(a, b):
    return a + b

print(soma(1, 2))

def subtracao(a, b):
    return a - b

print(subtracao(1, 2))


def multiplicacao(a, b):    
    return a * b
