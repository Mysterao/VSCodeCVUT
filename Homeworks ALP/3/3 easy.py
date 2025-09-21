import random
list = [11, 13, 25, 40, 17, 35, 7, 100, 5, 2, 40, 75,
        73, 125, 20, 43, 41, 53, 55, 59]
list = [2, 7, 9, 13, 11, 20]

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

# for i in range(20):
#     n = random.randint(0, 300)
#     list.append(n)
# print(list)

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
    # print(matrix)
    # print(index_max_length)
    final_divisors = []
    for i in range(len(matrix[index_max_length])):
        number = matrix[index_max_length][i]
        in_all_lists = True
        for j in range(len(matrix)):
            if index_max_length != j:
                if number not in matrix[j]:
                    in_all_lists = False
        if in_all_lists == True:
            for j in range(len(matrix)):
                if index_max_length != j:
                    if number in matrix[j]:
                        matrix[j].pop(matrix[j].index(number))
                        matrix[j].append(0)
        if in_all_lists == True:
            final_divisors.append(number)
    # print(final_divisors)
final_number = 1
if len(final_divisors) == 1:
    final_number += -1 + final_divisors[0]
if len(final_divisors) > 1:
    for i in range(len(final_divisors)):
        final_number *= final_divisors[i]
print(final_number)