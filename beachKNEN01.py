#beach - Kaylee & Eloge
from graphics import*

beachWin = GraphWin("Beach!" , 900, 500)
beachWin.setCoords(0,0,900,500)

#Sky
skyRec = Rectangle(Point(0, 250), Point(900, 500))
skyRec.setFill("light blue")
skyRec.draw(beachWin)

#Sun
sunCir = Oval(Point(150, 420), Point(750, 90))
sunCir.setFill("yellow")
sunCir.draw(beachWin)

#Sand
sRec = Rectangle(Point(0, 0), Point(900, 100))
sRec.setFill("orange")
sRec.draw(beachWin) 

#Water
wRec = Rectangle(Point(0, 100), Point(900, 250))
wRec.setFill("dark blue")
wRec.draw(beachWin)

#Fish One
#fish tail
fishTail = Polygon(Point(700,130), Point(760,150), Point(760,110))
fishTail.setFill("magenta")
fishTail.draw(beachWin)

#fish body
fishBody = Oval(Point(695,150), Point(745,110))
fishBody.setFill(color_rgb(0,175,200))
fishBody.draw(beachWin)

#fish eye
fishEye = Circle(Point(700,135), 4)
fishEye.setFill("black")
fishEye.draw(beachWin)





