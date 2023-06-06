direcao = input("Digite 'encode' para codificar e 'decode' para descodificar.\n")
texto = input("Digite a sua mensagem.\n").lower()
espaco = int(input("Quantas casas de locomocao terá?\n"))


def cesar():
    texto_fin = ""
    if direcao == "encode":
        for letter in texto:
            posicao = ord(f"{letter}")
            nova_posicao = posicao + espaco
            nova_letra = chr(nova_posicao)
            texto_fin += nova_letra
        print(f"The encoded text is {texto_fin}")
    elif direcao == "decode":
        for letter in texto():
            posicao = ord(f"{letter}")
            nova_posicao = posicao - espaco
            nova_letra = chr(nova_posicao)
            texto_fin += nova_letra
        print(f"The decoded text is {texto_fin}")


cesar()
