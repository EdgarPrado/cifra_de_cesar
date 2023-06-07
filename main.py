continue_ = True
while continue_:
    direcao = input("Digite 'encode' para codificar e 'decode' para descodificar.\n")
    texto = input("Digite a sua mensagem.\n").lower()
    espaco = int(input("Quantas casas de locomocao terá?\n"))

    def cesar():   
        texto_fin = ""
        if direcao == "encode":
            for letter in texto:
                if letter == " " in texto: # Se caso o char for um espaço em branco -
                    texto_fin += " " #- o espaço não será modificado
                else:    
                    posicao = ord(f"{letter}") # Transformação de Letra para Posição na Tabela ASCII
                    nova_posicao = posicao + espaco # Mudando a Posição de Acordo com o espaço definido
                    nova_letra = chr(nova_posicao) # Transformação da Nova Posição para Nova Letra na Tabela ..
                    texto_fin += nova_letra # Processo de Juntar as Letras Modificadas.
            print(f"The encoded text is {texto_fin}")
        elif direcao == "decode":
            for letter in texto:
                if letter == " " in texto:
                    texto_fin += " "
                else:
                    posicao = ord(f"{letter}")
                    nova_posicao = posicao - espaco
                    nova_letra = chr(nova_posicao)
                    texto_fin += nova_letra
            print(f"The decoded text is {texto_fin}")
    vontade = True
    cesar()
    result = input("Você quer tentar de novo? (s/n)").lower()
    if result == "s":
        continue
    else:
        print("Entendido! Tenha um Bom Dia!")
        continue_ = False