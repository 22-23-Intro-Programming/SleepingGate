import random
from graphics import *
from grid_test import *
from fish import *

class shark:

    def __init__(self, shark_x, shark_y, win):
    #Here is the constructor method of the shark. We were going to use shark_grid as our conversion of
    #pixel coordinates to grid coordinates to make calculations more organized, rather than putting larger
    #numbers like 20 and 40. As you can see where we define I, we were testing to see if we could just assign
    #random x and y values, then multiply it by 20, and have 590 subtract by that number to get an odd number
    #that corresponded to a pixel x and y value that were within the squares. The minimum is 10, and the maximum
    #is 590. Later, when we actually were able to implement this on a basic level, we were planning to make a new method
    #that randomized the coordinates again if the coordinates were the same as another object's. So, it would actively check
    #all of their x and y values to see if they are equal. This would likely utilize a list, and a while loop, actively checking
    #the elements against each other, but the x and y coordinates of each object would have their own lists, but if the x values are
    #the same, it activates the next while loop of the y list, if the same two indices of both lists have the same element values,
    #it would perform the random.randint stuff all over again. Note that all of this stuff would be in the main grid module rather than
    #in a specific module like shark's.
        
        self.shark_x = shark_x
        

        self.shark_y = shark_y
       

        self.shark_grid_x = (shark_x - 110) // 20

        self.shark_grid_y = (shark_y - 110) // 20

        x = random.randint(0, 30)
        y = random.randint(0, 30)
        

        
        I = Image(Point(shark_x, shark_y), "shark.png")
        I.draw(win)


        #I = Image(Point(590 - (shark_x * 20), 590 - (shark_y * 20)), "shark.png")
        #I.draw(win)          




def possible_moves():



    moveOptions = []


    maximum_distance = 2
            
    for x_moves in range(-2, 3):
        
        for y_moves in range(-2, 3):
            
            distance = ((x_moves ** 2) + (y_moves ** 2) ** 0.5)

            if distance <= 5 and distance != 0:

                moveOptions.append((x_moves, y_moves))
    
                print(moveOptions)

                #for change_x, change_y in moveOptions:
                    
                #Here, instead of hard-coding movements into a list, we found a way to just
                #loop through all the possible movements using the range method. Because the minimum
                #movement of the x and y is -2, we start the range at -2, and because the max of the x
                #and y is 2, we end at 3. Then, we employ the distance formula to basically say that if the
                #specific x and y that go through the loop are squared, added to each other, then
                #square rooted, and that is less than or equal to 5 (and not equal to 0), then that movement is a
                #possible move, and hence, append it to the list of move options.
possible_moves()


def move():

    distance_1 = (((shark_grid_x - fish_1_grid_x) ** 2) + ((shark_grid_y - fish_1_grid_y) ** 2) ** 0.5)


    #This is sort of a conceptual method of what we were going to do with the shark's actual movement until we
    #hit a blockade of ideas. Basically, we were going to have three equations where the distance between the shark
    #and all three fishes was going to be calculated, then put into a list where you could then find the minimum
    #element of that list. The minimum would be the fish with the shortest distance between itself and the shark,
    #which would therefore be the first fish the shark would effectively lock onto and chase. As we can see here,
    #the distance is calculated using the distance formula, which is (distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)).
    #The reason we thought the distance formula would be the best is that it calculates the distance using both x and y,
    #rather than just one, which allows us to be exact in our calculations.

    #After it would find the fish with the shortest distance, it would refer back to the previous possible_moves
    #method, and then perform calculations with each one to see which would give the shark the shortest distance between
    #itself and the fish. Whichever one provides the minimum distance is the one the shark actually uses. That's sort of it
    #but despite having generally good ideas, we were still hit with other basic issues that continually held us back from even
    #having much of a chance at seeing these ideas come to fruition.





                
                
