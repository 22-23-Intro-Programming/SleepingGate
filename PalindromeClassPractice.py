def palindrome():
    answer = input("Write something you think is a Palindrome\n")

    last = len(answer)-1
    start = answer[0]

    i = 0
    for char in answer:
        if (answer[0+i] != answer[last-i]):
                return False
        i = i + 1
    return True    

        

    # -1 is always the last letter because it's one to the left
    # of 0, so we can use the length command to manipulate this.
    

    #\n creates a new line which the user can type

def main():
    
    print(palindrome())
    
if(__name__ == "__main__"):
    main()    
