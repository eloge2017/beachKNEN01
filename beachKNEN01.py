#beach - Kaylee & Eloge
from graphics import*

beachWin = GraphWin("Beach!" , 900, 500)
beachWin.setCoords(0,0,500,500)

#Sand
sRec = Rectangle(Point(0, 0), Point(500, 100))
sRec.setFill("orange")
sRec.draw(beachWin) 

#Water
wRec = Rectangle(Point(0, 100), Point(500, 300))
wRec.setFill("dark blue")
wRec.draw(beachWin) 
