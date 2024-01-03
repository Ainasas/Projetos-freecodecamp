"""
frase = str(input("Digite uma frase e eu direi quantas palavras existem nela: "))
x = len(frase.split())
print(x)
"""

with open("exemplo.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    print(len(conteudo.split()))