def main():

    type_of_operation = input()#receber o tipo de operação que vai ser executada

    matriz = []
    #vai receber os valores
    for i in range(12):
        line = []
        for j in range(12):
            line.append(float(input()))
        matriz.append(line)

    line = acima_daigonal(matriz)
    #calcular tudo
    final_result = array_operation(type_of_operation,line)
    #exibir resultado
    print(round(final_result,1))


def acima_daigonal(matrix):
    line = []

    for i in range(len(matrix)):
        operation = False
        for j in range(len(matrix[i])):
            if operation:
                line.append(matrix[i][j]) 
            if operation == False and i == j:
                operation = True
    
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
