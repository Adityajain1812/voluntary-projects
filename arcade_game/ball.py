from turtle import Turtle


class Ball(Turtle):

    # Created function for turtle movements
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Function for ball to movements along diagonal x and y axis
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    #  Function to bounce the ball as it touches the paddle and slightly increase its speed
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Reseting ball position to (0, 0) as any paddle misses the ball and reseting balls speed to normal 
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
