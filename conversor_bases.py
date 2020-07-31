"""
This code convert num in any base to other base

Example:

110010.101 2 base

50.625 in 10 base
"""

num = input("Give me a num: ")
base = int(input("Give me the base of number: "))
baseTo = int(input("Give me the base to convert: "))
num = num.split(".") #Separete the parts of the n

total = 0

auxNum = num[0]
weight = len(auxNum)

for number in auxNum:
    weight -= 1
    total += int(number)*(base**(weight))

if len(num) == 2:
    auxNum = num[1]
    weight = len(auxNum)
    
    for index in range(1,weight+1):
        exponent = int("-"+str(index))
        total += int(auxNum[index-1])*(base**(exponent))

numToBase = total.split(".")

numToBaseFirst = numToBase[0]

numToBaseSecond = numToBase[1]

def toBase(number, base):
    total = ""
    while True:
        total_aux = number
        module = number % base
        number = number // base
        total += str(module)

        if (total_aux // base ) < base:
            total += str(total_aux // base)
            return total[::-1]
     
if baseTo != 10:
    print("The number is: ", toBase(numToBaseFirst, baseTo), ".", toBase(numToBaseSecond, base))
elif baseTo > 10:
    print("This program only work until base 10")
else
    print("The number is: ", total)
    
