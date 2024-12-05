from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 21, "bold")

with open('../../../sabesh/Desktop/highscore.txt', 'r') as file:
    # Read the entire file
    highscore = file.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.highscore = int(highscore)
        self.teleport(x=0, y=270)
        self.score_update()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('../../../sabesh/Desktop/highscore.txt', 'w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_update()


    def game_over(self):
        self.teleport(0,0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
