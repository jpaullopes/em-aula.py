#faz cifra de cesar modificada / cada letra vai voltar determinado numero de casas segundo a posição
def cesar_cipher(characters,positions):
    
    #65-90
    new_word = ''
    for c in characters:

        ascii_positon = ord(c)
        new_position = ascii_positon - positions
        if new_position < 65:
            new_position += 26
        
        new_word += chr(new_position)

    return new_word

def main():
    number_count = int(input())

    for t in range(number_count):
        word = str(input())
        position = int(input())

        new_cesar = cesar_cipher(word,position)

        print(new_cesar)


main()
