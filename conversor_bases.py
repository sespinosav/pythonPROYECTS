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

numToBase = ""
if  (baseTo != 10):
    while True:
        total_aux = total
        module = total % baseTo
        total = total // baseTo
        numToBase += str(module)

        if (total_aux // baseTo ) < baseTo:
            numToBase += str(total_aux // baseTo)
            break

    print("The number is: ", numToBase[::-1])

else:
    
    print("The number is: ", total)

