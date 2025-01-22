from turtle import Turtle
ALLIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,260)
        self.color('white')
        self.score = 0
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', move=False, align=ALLIGNMENT, font=FONT)
