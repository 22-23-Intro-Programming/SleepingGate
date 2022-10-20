class Cat():
    def __init__(self, name, stupidity, cuteness, clumsiness):
        self.name = name
        self.stupidity = stupidity
        self.cuteness = cuteness
        self.clumsiness = clumsiness

    def getName(self):
         return self.name

    def getStupidity(self):
         return self.stupidity

    def getCuteness(self):
         return self.cuteness
        
    def getClumsiness(self):
         return self.clumsiness

def main():

    C = Cat("Minori", "100%", "200%", "1000%")
    D = Cat("Ms. Kitty", "0%", "300%", "300%")
    F = Cat("Gato", "-50%", "400%", "50%")

    print("Hi cat, what is your name?")

    print(C.getName())

    print("Hi other cat, what is your name")

    print(D.getName())

    print("Hi third cat, what is your name?")

    print(F.getName())

    print("Cat Stupidity Levels: ")
    print(C.getName() + ": " + str(C.getStupidity()))
    print(D.getName() + ": " + str(D.getStupidity()))
    print(F.getName() + ": " + str(F.getStupidity()))

    print("Cat Cuteness Levels: ")
    print(C.getName() + ": " + str(C.getCuteness()))
    print(D.getName() + ": " + str(D.getCuteness()))
    print(F.getName() + ": " + str(F.getCuteness()))

    print("Cat Clumsiness Levels: ")
    print(C.getName() + ": " + str(C.getClumsiness()))
    print(D.getName() + ": " + str(D.getClumsiness()))
    print(F.getName() + ": " + str(F.getClumsiness()))






if(__name__ == "__main__"):
    main()
