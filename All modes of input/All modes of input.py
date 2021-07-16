# all modes of input like this : in) ABC // out)ABC, ACB, BCA, BAC, CAB, CBA
# تمام حالت هاي موجود يک ورودي، مثال در بالا

# save outs in txt file next to the this file that named "pssword list.txt"
# ذخیره میکند "password list.txt" خروجي هارو در يک فايل کنار همين فايل به نام

import os
from random import *
obj = input("Enter object : ")
objL = list(obj) 
setNum = set()
while len(setNum) != len(objL)**3 : 
    rand = choices(obj,k=len(objL)) 
    join = "".join(rand)
    setNum.add(join)
listNum = list(setNum)
listNum_c = listNum[:]
join_list = "-".join(listNum_c)
with open('pssword list.txt','w') as data_file:
    data_file.write(
        join_list.replace("-","\n")
)
os.startfile('pssword list.txt')

