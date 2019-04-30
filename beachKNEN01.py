#beach - Kaylee & Eloge
from graphics import*

beachWin = GraphWin("Beach!" , 900, 500)
beachWin.setCoords(0,0,900,500)

def draw_Fish(xPos,yPos,fishCol1,fishCol3,fishCol2,Win):
    #x = 695
    #y = 150
    
    #fish tail
    fishTail = Polygon(Point(xPos+5,yPos-20), Point(xPos+65,yPos), Point(xPos+65,yPos-40))
    fishTail.setFill(fishCol1)
    fishTail.draw(Win)

    #fish body
    fishBody = Oval(Point(xPos,yPos), Point(xPos+50,yPos-40))
    fishBody.setFill(fishCol3)
    fishBody.draw(Win)

    #fish eye
    fishEye = Circle(Point(xPos+5,yPos-15), 4)
    fishEye.setFill(fishCol2)
    fishEye.draw(Win)


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


#draw the fish 
draw_Fish(750,150,"magenta","red","black",beachWin)
draw_Fish(100,200,"yellow","pink","black",beachWin)
draw_Fish(400,175,"pink","orange","black",beachWin)
draw_Fish(300,210,"blue","light green","black",beachWin)
draw_Fish(550,205,"light blue","yellow","black",beachWin)
