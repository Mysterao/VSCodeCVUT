list = list(map(int, input().split()))

currentlength = 0
currentsum = 0
    
longest = 0
longestsum = 0
longestindex = 0
value = False

for i in range(len(list)):
    currentnumber = int(list[i])
    if currentnumber%3 == 0:
        currentlength += 1
    if currentnumber%3 != 0 or i == len(list)-1: #adds the last number to the order if it´s divisible by 3
        if currentnumber%3 == 0: # We need to add one to the iterable value because of the last element fo the list being even
            i += 1
        if currentlength > longest:
            longest = currentlength # changes the last longest element to the current longer one
            longestindex = i-longest # changes the index of first element in the longest order
            for j in range(longest):
                currentsum += int(list[i-longest+j]) #sums the last "longest" length of elements
            longestsum = currentsum
            currentsum = 0
            value = True
        if currentlength == longest and value != True:
            for j in range(currentlength):
                currentsum += int(list[i-currentlength+j])
            if currentsum >= longestsum:
                longest = currentlength
                longestindex = i-longest
                longestsum = currentsum
            currentsum = 0
        currentlength = 0
    value = False
if longest == 0:
    print(0, 0, 0)
else:
    print(longestindex, longest, longestsum)