from turtle import Screen, Turtle
from paddle import  Paddle
from ball import Ball
import time
from score import ScoreBoad
from developer import DevName

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoad()
name = DevName()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down , "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down , "s")
game_speed  = 0.1

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        game_speed -= 0.2

    #Detect when r paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #Detect when l paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()