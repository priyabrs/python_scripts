from turtle import Turtle
ALIGNMENT = 'center'
FONT_TUPLE = ('Arial', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, color = 'white') -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color(color)
        self.write_score()

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self) -> None:
        self.write(f'Score: {self.score}', False, align = ALIGNMENT, font = FONT_TUPLE)

    def game_over(self) -> None:
        self.goto(0,0)
        self.write(f'GAME OVER !!!', False, align = ALIGNMENT, font = FONT_TUPLE)