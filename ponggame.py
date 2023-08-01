import turtle

W = turtle.Screen()
W.title("Pong game by ChinD")
W.bgcolor("blue")
W.setup(width=800, height=600)
W.tracer(0)

#Tools
tools = turtle.Turtle()
tools.speed(0)
tools.color("red")
tools.penup()
tools.hideturtle()
tools.goto(0, 260)
tools.write("Player 1:0  Player 2:0",align="center", font=("Ariel", 24, "normal"))

#Score
score_1 = 0
score_2 = 0
#Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len= 1)
paddle_1.color("yellow")
paddle_1.penup()
paddle_1.goto(-350, 0)

#Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len= 1)
paddle_2.color("yellow")
paddle_2.penup()
paddle_2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.25
ball.dy = -0.25

#Function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 30
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 30
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 30
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 30
    paddle_2.sety(y)
#Binding keyboard 
W.listen()
W.onkeypress(paddle_1_up, "w")
W.onkeypress(paddle_1_down, "s")
W.onkeypress(paddle_2_up, "Up")
W.onkeypress(paddle_2_down, "Down" )

#Main loop
while True:
    W.update()

    #How the ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #When the ball hit the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        tools.clear()
        tools.write("Player 1:{}  Player 2:{}".format(score_1, score_2),align="center", font=("Ariel", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        tools.clear()
        tools.write("Player 1:{}  Player 2:{}".format(score_1, score_2),align="center", font=("Ariel", 24, "normal"))

    #When the paddle hit the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

##Still have errors in games 
##When the left paddle hit and the player keep the two paddle out of the border, the ball will automatically bounce without the paddle
##Sometimes the balls will automatically bounce without the paddle
## The Pong game can be develop  