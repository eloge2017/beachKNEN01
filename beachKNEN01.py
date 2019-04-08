#beach - Kaylee & Eloge
from graphics import*

beachWin = GraphWin("Beach!" , 900, 500)
beachWin.setCoords(0,0,900,500)

def draw_Rec(rX, rY, size, color, win):
     rectangle = Rectangle(rX,rY)
     rectangle.setFill(color)
     rectangle.draw(win)


def draw_Cir(cX, cY, size, color, Win):
     for i in range (10): 
        circle = Circle(Point(cX, cY),(85))
        circle.setFill(color)
        circle.setOutline(color)
        circle.draw(Win)
        
#Sky
draw_Rec(Point(0, 250), Point(900, 500), 50,"light blue", beachWin)
     
#Sun
sunCir = Oval(Point(150, 430), Point(750, 90))
sunCir.setFill("yellow")
sunCir.draw(beachWin)

#Sand
draw_Rec(Point(0, 0), Point(900, 100), 50, "orange", beachWin)
 
#Water
draw_Rec(Point(0, 100), Point(900, 250), 50, "dark blue", beachWin)

size=70
for z in range(10):
    draw_Cir(z * 100,185 , size, "dark blue", beachWin)
