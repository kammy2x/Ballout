xCoordinate = 50
speed = 2
ellipseSize = 50
yCoordinate = 50
yspeed = 2
def setup():
    size(400,400)

def draw():
    k= random(23, 50)
    background(0)
    global xCoordinate, speed, ellipseSize, yCoordinate, yspeed
    leftTopBoundary = ellipseSize / 2
    rightBottomBoundary = 400 - ellipseSize / 2
    if xCoordinate >= rightBottomBoundary  or xCoordinate <= leftTopBoundary:
        speed = - speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
        yspeed = -yspeed
    xCoordinate +=speed
    yCoordinate +=speed
    fill(230, 200, 210)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
