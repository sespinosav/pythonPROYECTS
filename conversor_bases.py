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

if base != 10:
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
else: 
    total = num


print(total)
numToBase = str(total).split(".")

numToBaseFirst = numToBase[0]

numToBaseSecond = numToBase[1] if "." in str(total) else ""

def toBase(number, base):
    if number == "":
        return ""
    
    number = int(number)
    total = ""
    while True:
        total_aux = number
        module = number % base
        number = number // base
        total += str(module)

        if (total_aux // base ) < base:
            total += str(total_aux // base)
            return total[::-1]
print(numToBaseFirst,numToBaseSecond)     
if baseTo < 10 and baseTo != 10 and numToBaseSecond != "":
    print("The number is:", toBase(numToBaseFirst, baseTo) +  "." + toBase(numToBaseSecond, baseTo))

elif baseTo > 10:
    print("This program only work until base 10")

elif baseTo != 10:
    print("The number is: ", toBase(numToBaseFirst,baseTo))

else:
    print("The number is: ", total)
    
