print('Olá, este programa converte graus celcius para fahrenheit!\n')

querConverter = True
while querConverter:
    
    digitouCerto = False
    while not digitouCerto:
        try:
            celcius=float(input('Digite os graus em CELSIUS: '))
            
            if celcius<-273:
                print('O valor digitar é impossível de existir, tente novamente...\n')
            else:
                digitouCerto = True

        except ValueError:
            print('Digite apenas números, tente novamente! ...')

    fha=celcius*1.8+32
    print(f'{celcius} Graus Celsius equivalem a {fha} Graus Fharenheit!!\n')

    # Quer converter outro valor?

    digitouCerto = False
    while not digitouCerto:
        resposta = input("Quer converter outro valor? digite: ('S' ou 'N'): ")
        resposta = resposta.upper()

        if resposta!="S" and resposta!="N":
            print('Desculpe, não foi possível processar sua resposta. Tente novamente...\n')
        else:
            digitouCerto = True

    if resposta=="N": querConverter = False

print('Obrigado por utilizar este programa!')
