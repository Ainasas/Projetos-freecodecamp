org = input("Escreva o nome de uma organização: ").split()
sigla = ""
for n in range(len(org)):
    if org[n][0] == org[n][0].upper():
        sigla += org[n][0]
    
print(sigla)
    
    
