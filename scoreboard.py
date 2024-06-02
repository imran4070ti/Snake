from turtle import Turtle, TurtleScreen

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 285)
        self.hideturtle()
    

    def update_score(self):
        self.score+=1
    
    def get_score(self):
        return self.score

    def display_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    
    def refresh_scoreboard(self):
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=('Arial', 50, 'normal'))

