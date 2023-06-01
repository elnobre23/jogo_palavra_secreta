import os

contador_tentativas = 0
palavra_secreta = input('Escreva uma palavra para ser adivinhada pelo outro jogador: ')
os.system('cls')
letra_descoberta = ''
palavra_descoberta = ''

while True:
    letra_digitada = input('Informe uma letra para tentar descobrir a palavra secreta: ')
    contador_tentativas += 1
        
    if len(letra_digitada) != 1:
        print('Digite somente uma letra por vez!')
        continue
    
    if letra_digitada in palavra_secreta:     
        letra_descoberta += letra_digitada               
    else:
      print('A letra não está na palavra secreta') 
    
    palavra_formada = ''
    for i in palavra_secreta:
        if i in letra_descoberta:
            palavra_formada += i
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_secreta == palavra_formada:
        print(f'Parabéns! A palavra secreta era: {palavra_secreta}')
        print(f'Tentativas: {contador_tentativas}x')
        contador_tentativas = 0
        palavra_secreta = input('Escreva uma palavra para ser adivinhada pelo outro jogador: ')
        os.system('cls')
        letra_descoberta = ''
        palavra_descoberta = ''
