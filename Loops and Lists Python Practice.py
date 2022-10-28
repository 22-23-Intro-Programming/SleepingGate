def problem_1():
    input_list = input("Please enter numbers in the same format you would a list")

    input_list = input_list.replace(" ", "")

    input_list = input_list.replace(",", "")

    input_list = list(input_list)

    for numbers in (input_list):
        if input_list.count('7') >= 2:
                if input_list[input_list.index('7')] == '7':
                    if input_list[input_list.index('7') + 1] == '7':
                        boolean = ("True")
                    else:
                        boolean = ("False")
                        
# This took way too long for me to finally be able to do,
# I feel like a genius, but Thomas still exists 

                else:
                    boolean = ("False")
                
        else:
            boolean = ("False")

    print(boolean)         

    
def problem_2():
    input_list2 = input("Please enter numbers in the same format you would a list")

    input_list2 = input_list2.replace(" ", "")

    input_list2 = input_list2.split(',')

    #input_list2 = input_list2.replace(",", "")

    input_list2 = list(input_list2)
    
    summy = 0
    for numbers2 in range(len(input_list2)):
        if '0' in input_list2:
            if input_list2[int(numbers2)] == '0':
                break
                summy = summy + int(input_list2[numbers2])
                
            #[input_list2.index('0')] This would get the index of a given number, so this would give the index of number 0
            #if input_list2[input_list2.index(numbers2)] < input_list2.index('0'):
                #summy == sum(input_list2[numbers2] - input_list2.index(numbers2 >['0']))

            #Some old lines that I thought would work... but don't!
            #Love my life
            #The only issue is that it splits digits that have greater
            #than one number, so 66 would become 6, 6 and they would add unless
            #they're after the 0, which no numbers would be added after.
                

            else:
                summy = summy + int(input_list2[numbers2])
                


        else:
            summy = summy + int(input_list2[numbers2])




            
            #summy += int(numbers2)



    print(summy)           


def problem_3():
    input_list3 = input("Please enter numbers in the same format you would a list")

    input_list3 = input_list3.replace(" ", "")

    input_list3 = input_list3.split(',')

    input_list3 = list(input_list3)
    
    numbers3 = []
    summy2 = 0
    for numbers3 in range(len(input_list3)):
        if input_list3[int(numbers3)] == '2':
            if input_list3[int(numbers3)] == '3':
                summy2 == summy2 + int(input_list3[int(numbers3)]) - input_list3.index('2' < [numbers3] < '3')

            else:
                break
                summy2 == summy2 + int(input_list3[numbers3])        


        else:
            summy2 = summy2 + int(input_list3[numbers3])
            

            
            
        #if '2' in input_list3:
            #if input_list3[int(numbers3)] == '0':
               # break
                #summy2 = summy2 + int(input_list3[numbers3])

        #if '3' in input_list3:        



    print(summy2)


def main():
     x = input("Would you like to access Problem 1 (Consecutive 7's), Problem 2"
          "(After 0), or Problem 3 (2 and 3)?")
     if x == "Consecutive 7's":
         problem_1()
     if x == "After 0":
         problem_2()
     if x == "2 and 3":
         problem_3()

if __name__ == "__main__":
    main()


    
