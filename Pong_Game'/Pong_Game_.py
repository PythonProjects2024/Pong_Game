from turtle import Screen
from Modules.paddle import Paddle
from Modules.ball import Ball
from Modules.scoreboard import Scoreboard
import time


game_on= True

screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()


screen.setup(width=800, height=600)
screen.title("Welcom to the Pong Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "a")
screen.onkey(l_paddle.down, "z")



while game_on:
   screen.update()
   ball.ball_move()
   time.sleep(ball.move_speed)
   
     #Detection collision
   if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

        # Detection collision with paddle
   if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

   if ball.xcor() > 380:
       ball.reset_position()
       score.left_point()
   
   if ball.xcor() < -380:
       ball.reset_position()
       score.right_point()





screen.exitonclick()





