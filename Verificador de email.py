em = input("Digite o seu e-mail por favor: ")
fm = ['gmail', 'outlook', 'duck', 'ig']
for n in range(len(fm)):
    if em.count(fm[n]) > 0:
        print(f"Bem vindo, vejo que você tem um e-mail {fm[n]}.")
        break
    elif n == (len(fm) - 1):
        print("Seja bem vindo!")