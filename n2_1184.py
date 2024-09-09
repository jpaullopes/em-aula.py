def main():

    type_of_operation = input()#receber o tipo de operação que vai ser executada

    matriz = []
    #vai receber os valores
    for i in range(12):
        line = []
        for j in range(12):
            line.append(float(input()))
        matriz.append(line)

    line = abaixo_daigonal(matriz)
    #calcular tudo
    final_result = array_operation(type_of_operation,line)
    #exibir resultado
    print(round(final_result,1))


def abaixo_daigonal(matrix):
    line = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                line.append(matrix[i][j]) 
                

    return line


def array_operation(choice_operation,line):
    #selecionar o tipo de operação
    #usar o reduce
    if choice_operation == 'S':
        return my_reduce(lambda a,b: a + b,line,0)
    return my_reduce(lambda a,b:a + b,line,0) / len(line)
    #retornar resultado


def my_reduce(func,array,initial_value):
    #acomulador
    accomulator = initial_value 
    #iteração
    for i in array:
        #acomular cada valor
        accomulator = func(accomulator,i)
    #retorna
    return accomulator
            


main()
