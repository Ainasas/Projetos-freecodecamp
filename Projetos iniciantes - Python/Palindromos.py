palavras = []
palindromos = []
npalindromos = []
for n in range(5):
    palavras.append(input(f"Digite {5 - n} palavras e eu verificarei se são palindromos: "))
    if palavras[n][::-1] == palavras[n]:
        palindromos.append(palavras[n])
    else:
        npalindromos.append(palavras[n])
if len(palindromos) == 0:
    print("Nenhuma das palavras eram palindromos...")
else:
    print(f"As seguintes palavras são palindromos : {palindromos}")
    
    
    