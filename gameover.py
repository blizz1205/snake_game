from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.write("Конец игры!", align=ALIGMENT, font=FONT)


