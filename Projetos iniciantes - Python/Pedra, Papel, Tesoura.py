print("Bem vindo ao Pedra, Papel, Tesoura!")
j1 = input("Jogador 1, escolha 1 (pedra), 2 (papel) ou 3 (tesoura): ")
j2 = input("jogador 2, escolha 1 (pedra), 2 (papel) ou 3 (tesoura): ")
if j1 == '1' and j2 == '1':
    print('Empate')
elif j1 == '1' and j2 == '2':
    print('Jogador 2 venceu!!')
elif j1 == '1' and j2 == '3':
    print('Jogador 1 venceu!!')
elif j1 == '2' and j2 == '2':
    print('Empate')
elif j1 == '2' and j2 == '3':
    print('Jogador 2 venceu!!')
elif j1 == '2' and j2 == '1':
    print('Jogador 1 venceu!!')
elif j1 == '3' and j2 == '3':
    print('Empate')
elif j1 == '3' and j2 == '1':
    print('Jogador 2 venceu!!')
elif j1 == '3' and j2 == '2':
    print('Jogador 1 venceu!!')    
