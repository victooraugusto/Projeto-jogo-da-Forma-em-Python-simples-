import random

erros = 0  
limite_de_erros = 6  


lista_de_palavras = ['webcam', 'processador', 'monitor', 'mouse', 'teclado' ]
palavra_escolhia = random.choice(lista_de_palavras) 

espaco = ['_'] * len(palavra_escolhia) 


resposta = ' '
while (resposta != 'sim'):  
    resposta = input('Está pronto para jogar? ').lower()

while '_' in espaco and erros < limite_de_erros: 
    letra = input('Digite uma letra: ').lower() 
    acertou = False

    for i in range(len(palavra_escolhia)): 
        if letra == palavra_escolhia[i]:
            espaco[i] = letra 
            acertou = True

    if not acertou:
        erros += 1
        print(f'CUIDADO! VOCÊ ERROU! ERROS: {erros}/{limite_de_erros}')

    print(' '.join(espaco))

if '_' not in espaco:
        print("PARABÉNS! VOCÊ VENCEU!")
else: 
        print(f'VOCÊ PERDEU! A palavra era {palavra_escolhia}.')

