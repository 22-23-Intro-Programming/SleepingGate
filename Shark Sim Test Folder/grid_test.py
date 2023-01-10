from graphics import *
from shark_test import *
from fish import *
from Button import *
import random

   



def graph_horizontal(win):

    horizontal_lines = 0

    x_left = 100
    x_right = 500

    y_horizontal = 100

    while horizontal_lines < 21:
            
          line = Line(Point(x_left, y_horizontal), Point(x_right, y_horizontal))
          line.draw(win)
          y_horizontal += 20
          horizontal_lines += 1

          #This was the first method we made, graphing the horizontal
          #lines first. We did this by making two variables called x_left
          #and x_right, which we set equal to 100 and 500 respectively. This effectively
          #sets the boundaries for the horizontal lines, setting up a 100 pixel border between
          #itself and the window's border. The y value of the horizontal lines needs to start at 100
          #and incrementally increase by 20 to get a square size of 20-by-20 pixels. This required some
          #tweaking, but because we can visually see the changes we made, it was rather easy to fix
        

def graph_vertical(win):

    vertical_lines = 0

    y_top = 100
    y_bottom = 500

    x_vertical = 100
    
    while vertical_lines < 21:
            
          line = Line(Point(x_vertical, y_top), Point(x_vertical, y_bottom))
          line.draw(win)
          x_vertical += 20
          vertical_lines += 1

          #This works identically the same way with the horizontal lines, but the variables are switched
          #to x based variables. 
          

        
def main():

    ocean = GraphWin("Chess example", 600, 600)
    
    #random.randint(1, 30) == shark_x_ran
    #random.randint(1, 30) == shark_y_ran

    shark_x = random.randint(0, 30)
    shark_y = random.randint(0, 30)

   # fish_1_x_ran.int(1, 30) = fish_1_x_ran
   # fish_1_y_ran.int(1, 30) = fish_1_y_ran
   # fish_2_x_ran.int(1, 30) = fish_2_x_ran
   # fish_2_y_ran.int(1, 30) = fish_2_y_ran
   # fish_3_x_ran.int(1, 30) = fish_3_x_ran
   # fish_3_y_ran.int(1, 30) = fish_3_y_ran

    #ran_assurance_x = [shark_x_ran, fish_1_x_ran, fish_2_x_ran, fish_3_x_ran]

    #for randoms in range(len(ran_assurance_x)):
        
    #We explain all of this stuff in the shark's method

    shark_x = 590 - (shark_x * 20)
    shark_y = 590 - (shark_y * 20)

    
    
    graph_horizontal(ocean)
    graph_vertical(ocean)
    shark((shark_x * 20), (shark_y), ocean)
    #I = shark(590 - (shark_x * 20), 590 - (shark_y * 20), ocean)

    

    #And this. One thing I want to add is that we were also thinking about implementing
    #a button press to activate the random integer coordinates namely, the "Run" button.
    #The difference between the "Run" and "Next" is that "Next" activates their move
    #methods rather than "Run" activating the randomness.
    
         
    
    #fishes(Point(ran.fish1.x, ran.fish1.y), win)
    #fishes(Point(ran.fish2.x, ran.fish2.y), win)
    #fishes(Point(ran.fish3.x, ran.fish3.y), win)

    Q = Button(ocean, Point(100, 500), Point(150, 550), "tomato", "Quit")
    R = Button(ocean, Point(450, 500), Point(500, 550), "cyan", "Run")
    H = Button(ocean, Point(350, 500), Point(400, 550), "green", "Next")


    #These are our buttons for the graph which would do certain thing
               
     

if __name__ == "__main__":
    main()
