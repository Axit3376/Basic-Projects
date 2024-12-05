import turtle
from turtle import *
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update()
        self.hideturtle()


    def update(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, 'normal'))
    def inc_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", move=False, align="center", font=("Arial", 24, 'normal'))