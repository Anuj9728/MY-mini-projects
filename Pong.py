import turtle

wn = turtle.Screen()
wn.title("Pong by anuj kumar sharma")
wn.bgcolor("white")
wn.setup(width=1000, height=600)
wn.tracer(0) # stop the window from updating and we can manually update it


#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0) #speed of animation its maximum speed
paddle_a.shape("circle")
paddle_a.color("Red")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # paddle history will be deleted
paddle_a.goto(-450,0)
#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0) #speed of animation its maximum speed
paddle_b.shape("circle")
paddle_b.color("Green")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() # paddle history will be deleted
paddle_b.goto(+450,0)
#ball
ball=turtle.Turtle()
ball.speed(0) #speed of animation its maximum speed
ball.shape("circle")
ball.color("Black")
ball.penup() # paddle history will be deleted
ball.goto(0,0)
ball.dx = 0.4 #dx means delta x that is change in x pixel
ball.dy = -0.4

#function
#paddle a fn
def paddle_a_up():
    y=paddle_a.ycor() #.ycor return the coordinates to y 
    y += 15
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor() #.ycor return the coordinates to y 
    y += -15
    paddle_a.sety(y)
#paddle b fn
def paddle_b_up():
    y=paddle_b.ycor() #.ycor return the coordinates to y 
    y += 15
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor() #.ycor return the coordinates to y 
    y += -15
    paddle_b.sety(y)



#keybord binding
wn.listen()
wn.onkeypress(paddle_a_up ,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up ,"Up")
wn.onkeypress(paddle_b_down,"Down")


#main game loop
while True:
    wn.update() #update everytime the while loop run



    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)


    #border checking
    if ball.ycor()>  290: #top
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()< -290: # down
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor() > 500: #right
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -500: #left  
        ball.goto(0,0)
        ball.dx *= -1

    #paddle collision with ball
    if (ball.xcor() > 440 and ball.xcor() < 450 ) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(440)
        ball.dx *= -1

    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-440)
            ball.dx *= -1