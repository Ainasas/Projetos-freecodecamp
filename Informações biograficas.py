nome = input("Qual é seu nome? ")
if len(nome.strip()) < 3:
    print("seu nome não é valido, digite novamente:")
    nome = input()
idade = input("Quantos anos você tem? ")
try:
    int(idade)
except:
    print("Digite apenas números")
    idade = input(':')
endereço = input("Informe seu endereço: ")
if endereço.count(',') == 0:
    print("Seu endereço precisa ter número e estado.")
    endereço = input()
cpf = input("Digite seu CPF: ")
if len(cpf) < 9:
    print("Seu cpf é invalido, tente novamente")
    cpf = input()
print("Conferindo suas informações...")  
print("Tudo certo!!")