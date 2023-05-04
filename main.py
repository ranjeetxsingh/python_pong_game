from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

positions = [(0, -60), (0, -120), (0, -180), (0, -240), (0, -60), (0, 0), (0, 60), (0, 120),
             (0, 180), (0, 240)]

for position in positions:
    screen_break = Turtle("square")
    screen_break.shapesize(stretch_wid=1.75, stretch_len=.10)
    screen_break.penup()
    screen_break.setposition(position)
    screen_break.color("white")

pad_left = Paddle((-350, 0))
pad_right = Paddle((350, 0))
screen.update()

screen.listen()
screen.onkeypress(pad_left.up, "w")
screen.onkeypress(pad_left.down, "s")
screen.onkeypress(pad_right.up, "Up")
screen.onkeypress(pad_right.down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad_right) < 40 and ball.xcor() > 325 or ball.distance(pad_left) < 40 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
