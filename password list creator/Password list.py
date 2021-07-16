import os
import string
from random import *
from numpy import prod

setNum = set()
rangeNum = int(input('Enter length of password : '))
rangeList = range(int(rangeNum))
lines = int(input('Enter num of the output : '))
factorial = int(prod(list(num for num in range(1,rangeNum+1)))) #now is not currect
char_input = input("Enter char : (all, digits(0-9), letter(a-z A-Z), punc(&%..) : ").lower()
if "all" in char_input:
    char = string.digits + string.ascii_letters + string.punctuation

else:
    try:
        char = ''
        if 'digits' in char_input:
            char += string.digits 
        if 'letter' in char_input:
            char += string.ascii_letters
        if 'punc' in char_input:
            char += string.punctuation
    except:
        raise ValueError('invalid input')


while len(setNum)<= lines: #factorial - rangeNum
    password = "".join(choice(char)for x in rangeList) #password = "".join(choices(char,k=4))
    print(password)
    setNum.add(password)
listNum = list(setNum)
listNum_c = listNum[:]
join_list = "-".join(listNum_c)
with open('pssword list.txt','w') as data_file:
    data_file.write(
        join_list.replace("-","\n")
)
os.startfile('pssword list.txt')

