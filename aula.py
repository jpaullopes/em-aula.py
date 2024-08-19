from random import randint

#função geradora de outras funçoes
def with_sum_gerator(value):
    def new_funtion(number):
        return value + number
    
    return new_funtion


#função map
def my_map(func, array):
    new_list = []#nova coleção kkkkk

    for e in array:
        new_list.append(func(e))

    return new_list
    

def my_filter(func,array):
    new_array = []
    for element in array:
        if func(element):
            new_array.append(element)

    return new_array



def random_list(t,i,f):
    array = []
    for x in range(t):
        array.append(randint(i,f))
    
    return array


def filtrar_impar(numeros):
    #new_list = []
    #for e in numeros:
        #if e % 2 != 0:
            #new_list.append(e)
        
    #return new_list
    return numeros % 2 != 0

        #JS
        #if (e % 2 !== 0){
            #ew_list.push()
        #}


def elevator_number(number):
    return number ** 2


def main():
    list_ = random_list(10,1,100)
    print(list_)

    #JS - arraw function
    #const new_array = my_filter((n) => {return n % 2 != 0},list)
    new_array = my_filter(filtrar_impar, list_)
    new_array_two = my_map(elevator_number,list_)
    #new_array_two = my_map(lambda n : n ** 2,list)

    print(new_array)
    print(new_array_two)


main()
