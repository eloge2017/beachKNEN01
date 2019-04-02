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

Birds  
birdImage = Image(Point(250,370), "Unknown.png")
birdImage.draw(beachWin)

#Sand
sRec = Rectangle(Point(0, 0), Point(500, 100))
sRec.setFill("orange")
sRec.draw(beachWin) 

#Water
wRec = Rectangle(Point(0, 100), Point(500, 250))
wRec.setFill("dark blue")
wRec.draw(beachWin)


def draw_Cir(cX, cY, size, color, Win):
     for i in range (6): 
        circle = Circle(Point(cX, cY),(75))
        circle.setFill(color)
        circle.setOutline(color)
        circle.draw(Win)
   
size=70
for z in range(6):
    draw_Cir(z * 100,185 , size, "dark blue", beachWin)
