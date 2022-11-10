from graphics import*
from Button import*

def main():
    win = GraphWin("Character Creator", 800, 800)
    Face = Oval(Point(100, 100), Point(500, 700))
    Face.draw(win)

    eyes1 = Button(win, Point(525, 100), Point(625, 175), "cyan", "Big eyes")
    eyes2 = Button(win, Point(650, 100), Point(750, 175), "cyan", "Small eyes")

    nose1 = Button(win, Point(525, 200), Point(625, 275), "cyan", "Big nose")
    nose2 = Button(win, Point(650, 200), Point(750, 275), "cyan", "Small nose")
    
    QButton = Button(win, Point(600, 625), Point(750, 725), "red", "Quit")

    #Big Eyes
    Eye1 = Circle(Point(250,200), 50)
    Eye2 = Circle(Point(350,200), 50)

    #Small Eyes
    eye1 = Circle(Point(250,200), 20)
    eye2 = Circle(Point(350,200), 20)
    
    #Big Nose
    Nose1 = Polygon([Point(300,400), Point(325,425), Point(275,425)])
    Nose2 = Polygon([Point(300,400), Point(100,425), Point(425,425)])                
    
    eyes = [Eye1, Eye2, eye1, eye2]
    nose = [Nose1, Nose2]

    while True:
        m = win.getMouse()
        if eyes1.isClicked(m):
            for e in eyes:
                e.undraw()

            Eye1.draw(win)
            Eye2.draw(win)
            print("big eyes")

        elif eyes2.isClicked(m):
            for e in eyes:
                e.undraw()

            eye1.draw(win)
            eye2.draw(win)    
            print("small eyes")

        elif nose1.isClicked(m):
            for r in nose:
                r.undraw()

            Nose1.draw(win)

        elif nose2.isClicked(m):
            for r in nose:
                r.undraw()

            Nose2.draw(win)    

        elif QButton.isClicked(m):
            break
        
    win.close()   





    

if __name__ == "__main__":
    main()
