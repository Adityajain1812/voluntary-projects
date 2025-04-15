from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        
# Updating the score as snake eats the food
    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

# Reseting snake position as snake hit the wall or collide with its body
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

# Increasing the score as the player scores a point 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
