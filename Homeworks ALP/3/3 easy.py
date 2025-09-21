
list = [11, 13, 25, 40, 17, 35, 7, 100, 5, 2, 40, 75,
        73, 125, 20, 43, 41, 53, 55, 59]

def prime_number_tester(list):
    nonprime = []
    for i in range(len(list)):
        if list[i] == 2:
            continue
        if list[i]%2 == 0:
            nonprime.append(list[i])
            continue
        divisible = False
        j = 3
        upto = int(round(list[i]**(1/2), 0))
        while divisible == False:
            if j == upto:
                divisible = True
            if list[i]%j == 0:
                divisible = True
                nonprime.append(list[i])
            j += 1
    print(upto)
    if nonprime == None:
        return 1
    else:
        return nonprime

def divisors(element):
    divisors = []
    divided = False
    i = 2
    while divided == False:
        if element == i:
            divided = True
        if element%i == 0:
            divisors.append(i)
            element = element/i
            i = 2
            continue
        i += 1
    return divisors 

# for i in range(20):
#     n = int(input())
#     list.append(n)

list = prime_number_tester(list)
if list != 1:
    print(list)
    matrix = []
    index_max_length = 0
    max_length = 0
    for i in range(len(list)):
        list_of_divisors = divisors(list[i])
        matrix.append(list_of_divisors)
        if len(divisors(list[i])) >= max_length:
            index_max_length = i
            max_length = len(list_of_divisors)
    