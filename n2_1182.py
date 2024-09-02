def my_reduce(func,array,initial_value):
    #acomulador
    accomulator = initial_value 
    #iteração
    for i in array:
        #acomular cada valor
        accomulator = func(accomulator,i)
    #retorna
    return accomulator



def array_operation(choice_operation,choice_line,array):
    #pegar a linha escolhida
    line = array[choice_line]
    #selecionar o tipo de operação
    #usar o reduce
    if choice_operation == 'S':
        return my_reduce(lambda a,b: a + b,line,0)
    return my_reduce(lambda a,b:a + b,line,0) / len(array)
    #retornar resultado



def main():
    read_line = int(input())#receber a linha que vai ser lida
    type_of_operation = input()#receber o tipo de operação que vai ser executada

    matriz = []
    #vai receber os valores
    for i in range(12):
        line = []
        for j in range(12):
            line.append(float(input()))
        matriz.append(line)

    #calcular tudo
    final_result = array_operation(type_of_operation,read_line,matriz)
    #exibir resultado
    print(round(final_result,1))


main()
