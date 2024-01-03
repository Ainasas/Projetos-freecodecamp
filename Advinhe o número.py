import random
n = random.randint(1, 50)
jg = int(float(input("Eu escolhi um número entre 1 a 50, qual eu escolhi? ")))
tentativas = 1
while n != jg:
    if jg < 1 or jg > 50:
        jg = int(input("Valor invalido, tente um número entre 1 e 50: "))
        tentativas += 1
    else:
        jg = int(input("Ops...Você errou, tente novamente: "))
        tentativas += 1
    


print(f"Parabéns você ganhou, o número era {n} e você tentou {tentativas} vezes.")


