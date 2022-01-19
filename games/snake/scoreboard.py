from tkinter import N
from turtle import Turtle
from pathlib import Path

ALIGNMENT = 'center'
FONT_TUPLE = ('Arial', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, color = 'white') -> None:
        super().__init__()
        self.sb_color = color
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color(self.sb_color)
        self.high_score = self.get_highscore()
        self.write_score()
        

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self) -> None:
        self.write(f'Score: {self.score}     High Score: {self.high_score}', False, align = ALIGNMENT, font = FONT_TUPLE)

    def game_over(self) -> None:
        self.goto(0,0)
        self.write(f'GAME OVER !!!. \n Press \n  1. "y" to restart \n  2. "n" to exit ', False, align = ALIGNMENT, font = FONT_TUPLE)

    def get_highscore(self) -> int:
        high_score = 0
        highscore_file = Path('highscore.txt')
        if highscore_file.is_file():
            with open (highscore_file, 'r') as highscore_file:
                high_score = int(highscore_file.readlines()[0])
        return high_score

    def set_highscore(self, game_end = False) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        if game_end:
            highscore_file = Path('highscore.txt')
            with open (highscore_file, 'w') as highscore_file:
                highscore_file.write(str(self.high_score))
    
    def reset_scoreboard(self) -> None:
        self.set_highscore(True)
        self.clear()
        self.__init__(self.sb_color)
        # self.score = 0
        # self.penup()
        # self.hideturtle()
        # self.goto(0,270)
        # self.color(self.sb_color)
        # self.high_score = self.get_highscore()
        # self.write_score()
        


if __name__ == '__main__':
    sb = ScoreBoard()
    print(sb.high_score)
        