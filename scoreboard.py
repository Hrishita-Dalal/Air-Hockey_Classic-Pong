from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Comic Sans MS", 40, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Comic Sans MS", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def win(self, winner):
        self.goto(0, 0)
        self.write(f"Game Over\n{winner} won!", align="center", font=("Comic Sans MS", 30, "normal"))
