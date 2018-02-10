import turtle
wn = turtle.Screen()
wn.bgcolor("black")
turtle = turtle.Turtle()
turtle.speed(10)
turtle.penup()
turtle.shape("turtle")

def drawFillRectangle(x, y, length, width, color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def drawStar(x,y,color,length) :
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for turn in range(0,5) :
        turtle.forward(length)
        turtle.right(144)
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()


def drawStripes() :
    x = -230
    y = 125
    for stripe in range(0,6) :
        drawFillRectangle(x, y, 18, 460, 'red')
        y = y - 20
        drawFillRectangle(x, y, 18, 460, 'white')
        y = y - 19
    drawFillRectangle(x, y, 18, 460, 'red')
    y = y - 20

def drawSquare() :
    drawFillRectangle(-230, 125, 135, 150, 'navy')

def drawSixStars() :
    y = 115
    for row in range(0,5) :
        x = -230
        y = y - 4
        for star in range (0,6) :
            x = x + 6
            drawStar(x, y, 'white', 10)
            x = x + 19
        y = y - 20

def drawFiveStars() :
    y = 103
    for row in range(0,4) :
        x = -212
        y = y - 4
        for star in range (0,5) :
            drawStar(x, y, 'white', 10)
            x = x + 25
        y = y - 20

drawStripes()
drawSquare()
drawSixStars()
drawFiveStars()
turtle.goto(0,-140)
turtle.write("Go USA")
turtle.back(20)



