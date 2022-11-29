from graphics import *
from Button import *

def main():
    
    win = GraphWin("Palindrome", 800, 600)
    win.setBackground("beige")

    Q = Button(win, Point(650, 500), Point(750, 575), "red", "Quit")
    P = Button(win, Point(350, 350), Point(450, 425), "cyan", "Check!")

    E = Entry(Point(400, 300), 30)
    E.draw(win)

    T = Text(Point(400, 250), "Write something below that you think is a palindrome.")
    T.draw(win)

    #get_pal_value = "Whether or not it's a palindrome will appear here"
    Palinblock = Text(Point(400, 450), "")
    Palinblock.draw(win)

    pal = E.getText()
    while True:
        
        m = win.getMouse()

        if Q.isClicked(m):
            break
        
        if P.isClicked(m):
            pal = E.getText()
            #test pal for palindrome
            #have a GUI output
            
            pal = pal.casefold()
            check_rev = pal[::-1]

            if check_rev == pal:
                Palinblock.setText(pal + " is indeed a pally")
                
                
            else:
                Palinblock.setText(pal + " is not a pally")

           
                
            print(pal)
            

    win.close()    

        

    
if __name__ == "__main__":
    main()
