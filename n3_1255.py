def bubble_sort(array):
    # Cria uma cópia do array para evitar modificar o original
    new_array = array[:]
    n = len(new_array)
    # Itera sobre o array
    for j in range(n):
        for e in range(n - j - 1):
            # Troca os elementos se estiverem fora de ordem
            if new_array[e] > new_array[e + 1]:
                new_array[e], new_array[e + 1] = new_array[e + 1], new_array[e]
    return new_array


def remove_space(text):
    new_text = ''
    # Remove espaços do texto
    for c in text:
        if c != ' ':
            new_text += c
    return new_text


def letter_hight_frequence(text):
    list_used_letters = []
    temp_text = text.lower()  # Converte o texto para minúsculas
    characters = remove_space(temp_text)  # Remove espaços

    best_frequence = 0
    best_letter = ''

    # Conta a frequência de cada letra
    for c in characters:
        if c.isalpha() and c not in list_used_letters:  # Considera apenas letras não processadas
            temp_count = 0
            list_used_letters.append(c)
            # Conta quantas vezes a letra aparece no texto
            for x in characters:
                if c == x:
                    temp_count += 1
    
            # Atualiza a letra mais frequente
            if temp_count > best_frequence:
                best_frequence = temp_count
                best_letter = c
            elif temp_count == best_frequence:
                best_letter += c  # Adiciona a letra ao resultado em caso de empate

    # Converte a string de letras mais frequentes em uma lista
    temp_list = []
    for l in best_letter:
        temp_list.append(l)

    best_letter = ''
    # Ordena as letras mais frequentes
    temp_list = bubble_sort(temp_list)
    
    # Concatena as letras ordenadas em uma string
    for i in temp_list:
        best_letter += i

    return best_letter


def main():
    test_numbers = int(input())  # Lê o número de casos de teste

    for t in range(test_numbers):
        corrent_text = input()  # Lê o texto para o teste atual

        best_frequence = letter_hight_frequence(corrent_text)  # Obtém a(s) letra(s) mais frequente(s)

        print(best_frequence)  # Imprime a(s) letra(s) mais frequente(s)

main()
