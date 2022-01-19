from turtle import Screen

class GameScreen():
    def __init__(self, screen_name, bg_color = 'black', width = 600, height = 600) -> None:
        self.screen_name = screen_name
        self.bg_color = bg_color
        self.width = width
        self.height = height
        self.create_screen()

    def create_screen(self):
        screen = Screen()
        screen.setup(width=self.width, height=self.height)
        screen.bgcolor(self.bg_color)
        screen.title(self.screen_name)
        screen.tracer(0)