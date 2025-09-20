list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"]

# sustava = int(input("Input your number system : "))
# num1 = input("1st number : ")
# num2 = input("2nd number : ")
# num3 = input("3rd number : ")
sustava = 33
num1 = "pm.ttnp1"
num2 = "l.e12w"
num3 = "n.m6hqnq"

if "." not in num1:
    num1 += ".0"
if "." not in num2:
    num2 += ".0"
if "." not in num3:
    num3 += ".0"

# THE PROGRAM TESTS FOR ERRORS IN INPUT
# ------------------------------------------------
def base_tester(sustava, num1):
    dots = 0
    greater_than_base = False
    for i in range(len(num1)):
        if num1[i] == ".":
            dots += 1
            # continue #THIS IS POSSIBLE
        if num1[i] != ".": #THIS SHOULD BE ALSO POSSIBLE
            if list.index(num1[i]) >= sustava:
                greater_than_base = True
    if dots > 1:
        return "Error"
    if greater_than_base == True:
        return "Error"
    

def error_tester(sustava, num1, num2, num3):
    if len(num1.split(".")) > 2 or len(num2.split(".")) > 2 or len(num3.split(".")) > 2:
        return "Error"
    if base_tester(sustava, num1) == "Error" or base_tester(sustava, num2) == "Error" or base_tester(sustava, num3) == "Error":
        return "Error"
# -----------------------------------------------

# THE PROGRAM ADDS PADDING FOR NUMBERS THAT NEED IT
# ------------------------------------------------
def normalize(num1, num2):
    num1 = num1.split(".")
    num2 = num2.split(".")
    # THIS PART TESTS FOR THE PADDING
    # -------------------------------------------------------------
    if len(num1[0]) > len(num2[0]):
        num2[0] = "0"*(len(num1[0])-len(num2[0])) + num2[0]
        # num2 = ".".join(num2) # THIS JOIN IS BASICALLY USELESS
    if len(num2[0]) > len(num1[0]):
        num1[0] = "0"*(len(num2[0])-len(num1[0])) + num1[0]
        # num1 = ".".join(num1) # THIS ONE AS WELL
    if len(num1[1]) > len(num2[1]):
        num2[1] = num2[1] + "0"*(len(num1[1])-len(num2[1]))
        # num2 = ".".join(num2) # THIS JOIN IS BASICALLY USELESS
    if len(num2[1]) > len(num1[1]):
        num1[1] = num1[1] + "0"*(len(num2[1])-len(num1[1]))
        # num1 = ".".join(num1) # THIS ONE AS WELL
    if num1 != str:
            num1 = ".".join(num1)
    if num2 != str:
            num2 = ".".join(num2)
    return num1, num2
# ------------------------------------------------

def addition(sustava, num1, num2):
    num1, num2 = normalize(num1, num2)
    result_decimal = ""
    result_tens = ""
    num1 = num1.split(".")
    num2 = num2.split(".")
    
    add_remainder = False
    for i in range(len(num1[1])):
        number = list.index(num1[1][len(num1[1])-1-i])+list.index(num2[1][len(num2[1])-1-i]) #THE ACTUAL ADDITION
        if add_remainder == True:
            number += 1
            add_remainder = False
        if number >= sustava:
            number = number-sustava
            add_remainder = True
        result_decimal += list[number] # ADDS THE SUM OF 2 NUMBERS TO DECIMALS

    for i in range(len(num1[0])):
        number = list.index(num1[0][len(num1[0])-1-i])+list.index(num2[0][len(num2[0])-1-i]) #THE ACTUAL ADDITION
        if add_remainder == True:
            number += 1
            add_remainder = False
        if number >= sustava:
            number = number-sustava
            add_remainder = True
        result_tens += list[number] # ADDS THE SUM OF 2 NUMBERS TO TENS
    final = result_tens[::-1] + "." + result_decimal[::-1] # WE NEED TO REVERSE THE STRINGS
    if add_remainder == True:
        final = "1"+final
    return final

def comparator(n, system):
    if int(system) > 9:
        system = int(system)
    else:
        system = list.index(system)
    if len(n) > 2:
        return 0
    if len(n) == 2:
        pred = 0
        za = 0
        for i in range(len(n[0])):
            pred += list.index(n[0][len(n[0])-1-i])*(system**i)
        for i in range(len(n[1])):
            za += list.index(n[1][i])*(system**((-1*i)-1))
        za = str(za).split(".")[1]
        final = str(pred)+"."+za
        return float(final)
    if len(n) == 1:
        pred = 0
        for i in range(len(n[0])):
            pred += int(n[0][len(n[0])-1-i])*(system**i)
        return pred
    
    
def subtraction(sustava, num1, num2):
    num1, num2 = normalize(num1, num2)
    result = ""
    add_carry = False
    for i in range(len(num1)):
        if num1[len(num1)-1-i] != ".":
            number = list.index(num1[len(num1)-1-i]) - list.index(num2[len(num2)-1-i])
            if add_carry == True:
                number -= 1
                add_carry = False
            if number < 0:
                number += sustava
                add_carry = True
            result += list[number]
        if num1[len(num1)-1-i] == ".":
            result += "."
    result = result[::-1]
    return result

def normalize_final(number):
    done = False
    waszero_front = True
    waszero_back = True
    minus = False
    i = 0
    while done != True:
        if number[i] == "-":
            minus = True
        if minus == True:
            if number[i+1] == "0" and waszero_front == True:
                number = number[:i+1] + number[i+2:]
        if minus == False:
            if number[i] == "0" and waszero_front == True:
                number = number[i+1:]
        if number[len(number)-1-i] == "0" and waszero_back == True:
            number = number[:len(number)-1-i]
        else:
            waszero_front = False
            waszero_back = False
            if waszero_back == False and waszero_front == False:
                done = True
    if number[0] == ".":
        number = "0"+number
    return number

if error_tester(sustava, num1, num2, num3) == "Error":
    print("ERROR")
else:
    # print(subtraction(sustava, addition(sustava, num1, num2), num2))
    first_sum = addition(sustava, num1, num2)
    # print(first_sum)
    if comparator(first_sum.split("."), str(sustava)) < comparator(num3.split("."), str(sustava)):
        redacted = "-"+subtraction(sustava, num3, first_sum)
    # print(addition(sustava, first_sum, num3))
    if comparator(first_sum.split("."), str(sustava)) >= comparator(num3.split("."), str(sustava)):
        redacted = subtraction(sustava, first_sum, num3)
    # print(redacted)
    print(normalize_final(redacted))