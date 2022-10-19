# Problem 1: Greeting:

def Problem1():
    x = input("What is your name?")
    print(x)
    x = str(x)
    print("Ahh, " + str(x) + ", what an eloquent name! It is a pleasure to meet you!")


# Problem 2: isMultiple:

def Problem2(x, y):
    print("Please put your 2 numbers in")
    x = input("num1")
    y = input("num2")
    result = (int(x)%int(y))
    if result == 0:
        print("Indeed,", x ,"and", y ,"are multiples!")
    else:
        print("Unfortunately", x ,"and", y ,"are not multiples.")
        

# Problem 3: Palindrome:

def Problem3():
    word = input("Please enter a number, word, or phrase, and I will "
                  "tell you if it is a palindrome!")
    reverse = word[::-1]
    if reverse == word:
        print("Sí,", word ,"is indeed a Palindrome, sadly not the one from Destiny,"
              " that thing is really good.")
    else:
        print("No,", word ,"is not a Palindrome")
        

# Main Function (choose between different problems):

def main():
    x = input("Would you like to access Problem 1 (Greeting), Problem 2"
          "(Multiples), or Problem 3 (Palindrome)?")
    if x == "Greeting":
        Problem1()
    if x == "Multiples":
        Problem2(4, 3)
    if x == "Palindrome":
        Problem3()

if(__name__ == "__main__"):
    main()


