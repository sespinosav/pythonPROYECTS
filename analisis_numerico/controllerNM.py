class ControllerNM:
    def __init__(self, method=False, result=False):
        self.__method = method
        self.__result = result
    
    def setMethod(self, method):
        self.__method = method

    def getMethod(self):
        return self.__method
    
    def setResult(self, result):
        self.__result = result
    
    def getResult(self):
        return self.__result
    