class StringManipulator:
    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

s = StringManipulator()
s.getString()
s.printString()
