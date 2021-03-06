class ControllerConversor:
    def __init__(self, result=False):
        self.__result = result
        self.__css = "barona style"
    
    def setCSS(self, css):
        self.__css = css
    
    def getCSS(self):
        return self.__css

    def setResult(self,result):
        self.__result = result
    
    def getResult(self):
        return self.__result

    def conversor(self,data):
        num = data['n']
        base = int(data['o'])
        baseTo = int(data['t'])
        num = num.split(".") #Separete the parts of the number

        def to10Base(num, base, test="", comparate=""):
            """
            Description: transform any number into base 10 
            since first a base 10 is passed and then it can be taken to another base
            and if you pass comparison values with the test and comparate variables,
            identify if they are the same, to avoid creating periodic numbers later

            Type: boolean for comparation
            or list for only transformation

            Param:
                
                num: number for transformation
                base: original base of number
                test: original numbe if you need compare the numbers 
                comparate: this number will be transformed and evaluated
                later to verify if the desired number has already been reached

            Return:

                num: number for only transformation
                false: if when calculating the part after
                the point exceeds 98 units, we interrupt the comparison process
                float(num[0] + "." + num[1]) != float(test): We compare if the part after the point 
                we are calculating has already reached the expected result
            """

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
                    if len(comparate.split(".")[1]) > 100:
                        return False
                    return float(num[0] + "." + num[1]) != float(test)
            
            return num

        num = to10Base(num=num,base=base) #convert the original number to base 10

        #depending on whether the number has part after the point or not we choose how to process the data
        if len(num) == 2:
            numToBaseFirst = int(num[0]) #first part of the number, before point
            numToBaseSecond = int(num[1]) #second part of the number, after point
            num = float(num[0] + "." + num[1]) 

        else:
            numToBaseFirst = int(num[0])
            num = int(num[0])
            numToBaseSecond = ""

        testAux = num  #this constant keeps the original value of the number, since it will be modified later

        def toBaseFirst(number, base):
            """
            Description: Transform the first part of the number
            to the desired base using the division method and keeping the quotients

            Type: string

            Param:
                
                number: number for transformation
                base: final base

            Return:

                string whit number in desired base
            """
            if number == "": #if number empty so return empty result
                return ""
            
            number = int(number) #string number to int number
            total = "" #final result
            while True: #simulation for cicle do-while
                total_aux = number
                module = number % base
                number = number // base
                total += str(module)

                if (total_aux // base ) < base:
                    total += str(total_aux // base)
                    return total[::-1] # invert the string

        def toBaseSecond(number, base, first, toBase):
            """
            Description: Transform the second part of the number
            to the desired base using the multiplication method and
            keeping the part before the point after multiplication

            Type: string

            Param:
                
                number: number for transformation
                base: final base

            Return:

                string whit number in desired base
            """
            data = [] #numbers after point
            auxNumber = float("0." + str(number)) #number part after multiplication in each iteration

            totalFloat = auxNumber * base #total number after multiplication in each iteration

            total = first + "." + (str(totalFloat).split("."))[0] # storage for the final result and to compare if we have already reached the result

            while(((str(auxNumber).split("."))[1] != "0") and (to10Base("", baseTo, testAux, total))):
                totalFloat = auxNumber * base
                data.append((str(totalFloat).split("."))[0])
                auxNumber = float("0."+(str(totalFloat).split(".")[1]))

                total = ""

                for floatNumber in data:
                    total += floatNumber

                total = first + "." + str(total)

            index = 0 #position for first number diferent of 0 in the result
            for digit in total: 
                if digit != "0": # remove the zeros to the left
                    if index != 0:
                        return total[index-1:]
                    return total
                index += 1

        """
        depending on whether the number has part after the point
        or not or if it exceeds the base to which we can transform, one output or another is shown
        """

        if baseTo < 10 and baseTo != 10 and numToBaseSecond != "":
            first = toBaseFirst(numToBaseFirst, baseTo)
            return f"The number is: {toBaseSecond(numToBaseSecond, baseTo, first, base)}"

        elif baseTo > 10:
            return f"This program only work until base 10"

        elif baseTo != 10:
            return f"The number is: {toBaseFirst(numToBaseFirst,baseTo)}"

        else:
            return f"The number is: {testAux}"