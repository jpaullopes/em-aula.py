from random import randint

def random_list(t,i,f):
    array = []
    for x in range(t):
        array.append(randint(i,f))
    
    return array

def main():
    numbers = random_list(10,1,100)

    print(numbers)


main()
