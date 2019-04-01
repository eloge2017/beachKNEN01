#beach - Kaylee & Eloge
from graphics import*

beachWin = GraphWin("Beach!" , 900, 500)
beachWin.setCoords(0,0,500,500)



#Sky
skyRec = Rectangle(Point(0, 250), Point(500, 900))
skyRec.setFill("light blue")
skyRec.draw(beachWin)

#Sun
sunCir = Oval(Point(150, 400), Point(350, 100))
sunCir.setFill("yellow")
sunCir.draw(beachWin)

#Birds  
#birdImage = Image(Point(250,370), "Unknown.png")
#birdImage.draw(beachWin)

#Sand
sRec = Rectangle(Point(0, 0), Point(500, 100))
sRec.setFill("orange")
sRec.draw(beachWin) 

#Water
wRec = Rectangle(Point(0, 100), Point(500, 250))
wRec.setFill("dark blue")
wRec.draw(beachWin)


import random

def draw_Cir(cX, cY, size, color, Win):
     for i in range (6): 
        circle = Circle(Point(cX, cY),(size/6) * (i - 6))
        if i%2 == 0:
            circle.setFill(color)
        else:
            circle.setFill(color_rgb(0,0,0))
        circle.draw(Win)
   
size=70
for z in range(6):
    draw_Cir(z * 100,200 , size, "red", beachWin)

