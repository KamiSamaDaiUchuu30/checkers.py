from graphics import *

def square(pos, color):
    sq = Rectangle(Point(pos*(i+1), pos*(j+1)), Point(pos*(i+2),pos*(j+2)))
    sq.setFill(color_rgb(color, 0, 0))
    sq.draw(chWin)
    
   
sqSz = 50
red = 244
chWin = GraphWin("checkers", sqSz *10, sqSz *10)
chWin.setCoords(0, 0, sqSz*10, sqSz*10)

for j in range(8):
    if j %2 == 0:
        red = 244
    else:
        red = 0
            
    for i in range(8):
        square(sqSz,red)
        if red == 0:
            red = 122
        elif red == 244:
            red = 0
        red*=2
