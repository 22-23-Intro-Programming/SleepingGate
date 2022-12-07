from graphics import*
from Button import*

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            
            #if r  >= 205:
                #r = (r // 100) + r
                
            #else:
               # r += 50
                #g += 50
               # b += 50    

           # if g >= 205:
               # g = (g // 100) + g
                
            #else:
                #r += 50
                #g += 50
                #b += 50    

            #if b >= 205:
                #b = (b // 100) + b
                
            #else:
               # r += 50
                #g += 50
                #b += 50"   

                #newColor = color_rgb(r, g, b)
                
            if r >= 255:
                r = 255
                
            else:
                r += 50
                  

            if g >= 255:
                g = 255
                
            else:
                g += 50

            if b >= 255:
                b = 255

            else:
                b += 50   
                #newColor = color_rgb(r, g, b)
                #newColor = color_rgb(r + 50, g + 50, b + 50)
                
            newColor = color_rgb(r, g, b)    
            
            img.setPixel(i, j, newColor)

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            
            if r or g or b <= 50:
                r = r // 2
                g = g // 2
                b = b // 2
                newColor = color_rgb(r, g, b)
                
            else:    
                newColor = color_rgb(r - 50, g - 50, b - 50)
            
            img.setPixel(i, j, newColor)

def grayscalify(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]

            newColor = color_rgb((r+g+b) // 3, (r+g+b) // 3, (r+g+b) // 3)

            img.setPixel(i, j, newColor)

def contrastify(img):
    x = img.getWidth()
    y = img.getHeight()
            
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]

            if (r + g + b / 3) >= 175:
                r += 50
                g += 50
                b += 50

            else:
                r -= 50
                g -= 50
                b -= 50
                #newColor = color_rgb(r + 50, g + 50, b + 50)

                

            if r >= 255:
                r = 255
            

            if g >= 255:
                g = 255
    

            if b >= 255:
                b = 255


                

            if r <= 0:
                r = 0
                

            if g <= 0:
                g = 0
                

            if b <= 0:
                b = 0



            newColor = color_rgb(r, g, b)

            img.setPixel(i, j, newColor)
    
            

def main():
    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("beige")

    I = Image(Point(300, 300), "image.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "orange", "Darken")

    
    B2 = Button(win, Point(600, 200), Point(700, 275), "yellow", "Lighten")

    B3 = Button(win, Point(600, 300), Point(700, 375), "green", "Grayscalify")

    B4 = Button(win, Point(600, 400), Point(700, 475), "blue", "Contrastify")
    

    Q = Button(win, Point(600, 500), Point(700, 575), "red", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            grayscalify(I)

        if B4.isClicked(m):
            contrastify(I)

        if Q.isClicked(m):
            break
        
if __name__ == "__main__":
    main()
