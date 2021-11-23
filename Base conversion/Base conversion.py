

def convert(num, from_=10, to=2):
    
    if num > 1 and int(num) != num :
        int_part = convert(int(num))
        float_part = convert( num - int(num) )
        return f"{str(int_part)}.{str(float_part)[2:]}"

    if from_ != 10:
        num = int (convert(num, from_, 10))
    
    result = ""

    if from_ > to:
        if num < 1: 
            while num != 0:
                num *= to
                if num >= 1:
                    result += str(int(num))
                    num -= int(num)

                else:
                    result += "0"
                
            return float ( "0." + result)

        elif num > 1 :
            while num != 0:
                result += str(num % to)
                num = num // to

            return int (result[::-1])


    elif from_ == to:
        return int(num)

    elif from_ < to:
        
        if num < 1:            
            pass

        elif num > 1:
            pass


        return int(num)



# UnitTest

## from > to / num > 1
# print(convert(41, 10, 2))

## from > to / num < 1
# print(convert(0.513, 10, 8))
# print(convert(41.6875, 10, 8))



print(hex(15)[2:].upper())

