def Sreverse(iterable):
    stack = []
    
    #pushing
    for i in iterable:
        stack.append(i)

    reversedString = ""
    reversedList = []

    #poping
    for i in range(len(stack)):
        if type(iterable) == str:
            i = stack.pop()
            reversedString += i

        if type(iterable) == list:
            i = stack.pop()
            reversedList.append(i)

    return reversedString if type(iterable) == str else reversedList



print(Sreverse("mahdi"))
print(Sreverse([1,2,3,4]))
