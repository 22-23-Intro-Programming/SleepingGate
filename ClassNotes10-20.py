class Cat:

    # the constructor method, defines how the cat is initially created
    def __init__(self, name, age):
        # create instance variables
        self.fur = "fluffy"
        self.age = age
        self.color = "black"
        self.name = name

    def getAge(self):
         return self.age

    def getName(self):
         return self.name

        

        

def main():

    C = Cat("Mittens", 20)
    D = Cat("Leo", 3)

    print("Hi cat, what is your name?")

    print(C.getName())

    print("Hi other cat, what is your name")

    print(D.getName())

    print("Cat ages: ")
    print(C.getName() + ": " + str(C.getAge()))
    print(D.getName() + ": " + str(D.getAge()))



if(__name__ == "__main__"):
    main()    
