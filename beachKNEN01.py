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

#Fish One 
fishTail = Polygon(Point(430,130), Point(450,150), Point(450,110))
fishTail.setFill("magenta")
fishTail.draw(beachWin)

fishBody = Oval(Point(415,150), Point(445,110))
fishBody.setFill(color_rgb(0,175,200))
fishBody.draw(beachWin)



