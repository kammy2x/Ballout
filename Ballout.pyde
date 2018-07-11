yCoordinate = 50
xCoordinate = 50
yspeed = 6
xspeed = 8

ellipseSize = 50
def setup():
    size(400,400)

def draw():
    k= random(23, 50)
    background(0)
    global xCoordinate, yCoordinate, xspeed, yspeed, ellipseSize
    
    leftBoundary = ellipseSize / 2
    rightBoundary = 400 - ellipseSize / 2
    topBoundary = ellipseSize / 2
    bottomBoundary = 400 - ellipseSize / 2
    xCoordinate += xspeed
    yCoordinate += yspeed
    
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
        xspeed = -xspeed
        
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
        yspeed = - yspeed
    fill(57, 100, 130)
    ellipse(xCoordinate, yCoordinate, ellipseSize,ellipseSize)
    
