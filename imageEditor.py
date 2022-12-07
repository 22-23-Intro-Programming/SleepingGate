from graphics import*
from Button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            if r or g or b < 50:
                r = r // 2
                g = g // 2
                b = b // 2
                newColor = color_rgb(r, g, b)
            else:    
                newColor = color_rgb(r - 50, g - 50, b - 50)
            
            img.setPixel(i, j, newColor)
            

def main():
    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("beige")

    I = Image(Point(300, 300), "image.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "light red", "Darken")
    B.draw(win)
    
    B2 = Button(win, Point(600, 200), Point(700, 275), "cyan", "Lighten")
    B.draw(win)

    Q = Button(win, Point(600, 300), Point(700, 375), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        #if B2.isClicked(m):

        if Q.isClicked(m):
            break
        
if __name__ == "__main__":
    main()
