#variáveis
idade = 8
peso = 80.5
sexo = 'x'
nome = "joão"
print("idade = " + str(idade), "peso = " + str(peso),sexo, nome)
print(type(idade))
print(type(sexo))
print(type(nome))
#listas
nomes = ["Nilton","Pedro","Carlos","Nilton"] #mutáveis e permite itens duplicados
#conjuntos ou sets
anos = {1,2,3,4,5,6} #mutáveis, não ordenados e únicos não permite duplicata
#tuplas
frutas = ("banana", "maça", "banana") #imutáveis, permite duplicatas
#dicionários
cadastro = {"nome":"João Silva", 
            "idade":40, 
            "curso":"SI"
} #mutáveis, desordenados, chave única

for k,v in cadastro.items():
    print(k,v)

