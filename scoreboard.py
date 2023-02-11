from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("highscore.txt", "r") as hs1:
            self.high_score = int(hs1.read())
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"+++++++Score: {self.score} High Score: {self.high_score}++++++", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as hs:
                hs.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.high_score = self.score

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
