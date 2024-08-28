from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(position)


    # def l_move(self):
    #     move_y = self.xcor() + 20
    #     self.goto(0, move_y)

    def up(self):
        move_y = self.ycor() + 20
        self.goto(self.xcor(), move_y)
        
      

    def down(self):
        move_y = self.ycor() - 20
        self.goto(self.xcor(), move_y)
        
        


        
