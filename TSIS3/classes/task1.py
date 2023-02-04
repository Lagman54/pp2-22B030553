class SomeClass:
    currentInput = ""

    @classmethod
    def getString(cls):
        cls.currentInput = input()

    @classmethod
    def printString(cls):
        print(cls.currentInput.upper())


# SomeClass.getString()
# SomeClass.printString()
