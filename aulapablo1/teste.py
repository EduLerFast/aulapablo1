nome="matheus"
sobrenome="vinicius"

#concatenaçao
nome_completo= nome+" " +sobrenome
print (nome_completo)

nome_completo2= f"{nome}  {sobrenome}"
print (nome_completo2)


#fatiamento

print("primeira letra:", nome [0])
print("ultima 3 letras:", nome [1:45])


#metodos principais
print ("maiusculo:", nome.upper())
print ("minusculo:", nome.lower())
print ("titulo:", nome_completo.title())
print ("replace:", nome_completo.title().replace("Vinicius" , "Oliveira"))
print ("split:", nome_completo.split(" "))
print ("split:", nome_completo.split("a"))
print ("split:", nome_completo.split("i"))

print("################revisao inteiro##################")
idade=34

print(f'idade:{idade}')
print(f'idade X 2:{idade*2}')
print(f'idade:2:{idade/2}')
print(f'potencia:{idade**2}')
print(f'resto da divisao:{idade%5}')

#funçoes
print ("Minimo", min(3,7,1,2,3,5,7,4,2,9))
print ("Maximo", max(3,7,1,2,3,5,7,4,2,9))
print ("absoluto", abs(-20))
print ("Maximo", round(20.23892348238))


print("#################revisao float##################")
#operaçao com float

altura=1.71

print("altura:",altura)
print("altura X 2", altura*2)
print("altura : 3", altura/3)

print ("arredondamento:", round(altura,1))#quantidade de casas decimais

#biblioteca
import math
print ("raiz quadrada:", math.sqrt(16))
print ("PI:", math.pi)


print("#################revisao Boolean##################")
instrutor=True
ativo=False

#comparaçoes retornam boll
print("10 >5?", 10>5)
print("10 ==5?", 10==5)
print("10 <5?", 10<5)
print("10 !=5?", 10!=5)


#uso em if
if instrutor:
    print("é instrutor")
else:(" nao é instrutor")
print('verdade' if instrutor else "mentira")

print("################# REVISAO LISTA##################")
cores=['vermelho', 'azul','verde',]
print(cores)
#acesso e fatiamento
print('segunda cor segunda letra:', cores [1][1])
print('segunda cor segunda letra em diante:', cores [1][1:])

#metodos principais

#adiciona
cores.append("Amarelo")
print("Após append:", cores)


#remove
cores.remove("verde")
print ("Após remove:", cores)

print("quantidade", len (cores))
print("Existe 'amarelo'?", "Amarelo" in cores)


cores2 = cores.copy()
cores.append("laranja")

print('cores1', cores)
print('cores2', cores2)
cores2[0] = "Cinza"
print('cores2', cores2)

print("################# REVISAO tupla##################")
par = (1,2,4) #uma lista q NUNCA IRÁ MUDAR
print("primeiro",par[0])
print("ultimo",par[-1])
#par[0]=6       NAO FUNCIONA
print("comprimento", len(par))
print ("existe 3?", 3 in par)

print("################# REVISAO dicionario##################")
#chave: valor
config = {'modo':'aula', 'nivel': 'inicial'}
print(config)


print('nivel', config['modo'])
print('nivel', config.get("nivel"))

#adiçao/alteraçao
config['turma']='python 1'
print (config)

#Métodos princiais
print ('Chaves',config.keys())
print ('valores',config.values())
print ('items',config.items())



















