def factorial():
    num1 = input("Please enter a number you would like the factorial of")

    if int(num1) < 0:
        print("The factorials of all negative numbers are undefined")

    if int(num1) == 0:
        print("The factorial of 0 is always 1")

    if int(num1) == 1:
        print("The factorial of 1 is always 1")

    if int(num1) > 1:
        factorial = 1
        for i in range(1, int(num1) + 1): # Figured out how range actually works
            factorial *= i
        print(num1)#[::-1]) 
        # I couldn't figure out how to JUST make it print the last one (since
        # it for some reason prints multiple numbers), so the [::-1] shortcuts it
        # and just prints the last one. Sort of a crude fix, but it'll do.
        print("The factorial of " + str(num1) + " is " + str(factorial))
                          

def double_it():
    num2 = input("Please input a word, phrase, or number which "
                 "you would like to double each letter/number of")
    doubled = ""
    i = 0
    for i in range(len(num2)):
                doubled += num2[i] * 2
    print("The double word, phrase, or number that you entered is " + doubled[::-1])
    

def camel_case():
    file = input("Please input a file name that you would like to camel casify")
    new_camel = 1
    for i in range (len(file) -1):
        
        new_camel = file.title()
        
        new_camel = new_camel.replace(" ", "")
        
        new_camel = new_camel.replace("/", "-")

        new_camel = new_camel.replace(new_camel[0], new_camel[0].lower())
    print(new_camel)
    
        # Just like the previous solutions, the solutions are pretty crude, like
        # how I used replace() and title() to do something that the loop methods can
        # likely also do, as I've gone through everyone else's examples and seen they have
        


    
def main():
    x = input("Would you like to access Problem 1 (Factorial), Problem 2"
          "(Double It), or Problem 3 (Camel Case)?")
    if x == "Factorial":
        factorial()
    if x == "Double It":
        double_it()
    if x == "Camel Case":
        camel_case()

if __name__ == "__main__":
    main()
