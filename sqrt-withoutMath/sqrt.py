def Avr_jazr(x): 
    if (x == 0 or x == 1): 
        return x 
    i = 1 
    result = 1
    while (result <= x):
        i += 1
        result = i * i 
    return i - 1

def jazr(num1):
    num2 = Avr_jazr(num1)
    for i in range(11):
        num3 = num1 / num2
        num4 = num2 + num3
        num2 = num4 / 2
    return num2



print(Avr_jazr(13))


#© 2021 Arshia Ghayoumi, Inc.  XD
