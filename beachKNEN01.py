#beach - Kaylee & Eloge
from graphics import*

beachWin = GraphWin("Beach!" , 900, 500)
beachWin.setCoords(0,0,500,500)

#Sand
sRec = Rectangle(Point(0, 0), Point(500, 100))
sRec.setFill("orange")
sRec.draw(beachWin) 
