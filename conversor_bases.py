"""
This code convert num in any base to other base

Example:

110010.101 2 base

50.625 in 10 base
"""

num = input("Give me a num: ")
testAux = num
base = int(input("Give me the base of number: "))
baseTo = int(input("Give me the base to convert: "))
num = num.split(".") #Separete the parts of the n


def to10Base(num, base, test="", comparate=""):
    if test != "" and comparate != "":
        num = str(comparate).split(".")

    total = 0

    if base != 10:
        auxNum = num[0]
        weight = len(auxNum)

        for number in auxNum:
            weight -= 1
            total += int(number)*(int(base)**(weight))

        if len(num) == 2:
            auxNum = num[1]
            weight = len(auxNum)

            for index in range(1,weight+1):
                exponent = int("-"+str(index))
                total += int(auxNum[index-1])*(base**(exponent))

        num = str(total).split(".")

        if test != "" and comparate != "":
            if len(num[0] + "." + num[1]) > 100:
                return False
            return float(num[0] + "." + num[1]) != float(test)
    
    return num

num = to10Base(num=num,base=base)

if len(num) == 2:
    numToBaseFirst = int(num[0])
    numToBaseSecond = int(num[1])
    num = float(num[0] + "." + num[1])

else:
    numToBaseFirst = int(num[0])
    num = int(num[0])
    numToBaseSecond = ""

numToPrint = num

def toBaseFirst(number, base):
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

def toBaseSecond(number, base, first, toBase):
    data = []
    auxNumber = float("0." + str(number))

    totalFloat = auxNumber * base

    total = first + "." + (str(totalFloat).split("."))[0]

    while(((str(auxNumber).split("."))[1] != "0") and to10Base("", baseTo, testAux, total)):
        totalFloat = auxNumber * base
        data.append((str(totalFloat).split("."))[0])
        auxNumber = float("0."+(str(totalFloat).split(".")[1]))

        total = ""

        for floatNumber in data:
            total += floatNumber

        total = first + "." + str(total)

    return total

if baseTo < 10 and baseTo != 10 and numToBaseSecond != "":
    first = toBaseFirst(numToBaseFirst, baseTo)
    print("The number is:", toBaseSecond(numToBaseSecond, baseTo, first, base))

elif baseTo > 10:
    print("This program only work until base 10")

elif baseTo != 10:
    print("The number is: ", toBaseFirst(numToBaseFirst,baseTo))

else:
    print("The number is: ", numToPrint)
    
