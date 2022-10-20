import time
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

    print("\nHi cat, what is your name?")
    
    time.sleep(2)
    print("\n"+C.getName())

    time.sleep(4)
    print("\nHi other cat, what is your name?")

    time.sleep(2)
    print("\n"+D.getName())
    
    time.sleep(4)
    print("\nHi third cat, what is your name?")
    
    time.sleep(2)
    print("\n"+F.getName())
    
    time.sleep(4)
    print("\nCat Stupidity Levels: ")
    print("\n"+C.getName() + ": " + str(C.getStupidity()))
    print("\n"+D.getName() + ": " + str(D.getStupidity()))
    print("\n"+F.getName() + ": " + str(F.getStupidity()))
    
    time.sleep(4)
    print("\nCat Cuteness Levels: ")
    print("\n"+C.getName() + ": " + str(C.getCuteness()))
    print("\n"+D.getName() + ": " + str(D.getCuteness()))
    print("\n"+F.getName() + ": " + str(F.getCuteness()))

    time.sleep(4)
    print("\nCat Clumsiness Levels: ")
    print("\n"+C.getName() + ": " + str(C.getClumsiness()))
    print("\n"+D.getName() + ": " + str(D.getClumsiness()))
    print("\n"+F.getName() + ": " + str(F.getClumsiness()))






if(__name__ == "__main__"):
    main()
