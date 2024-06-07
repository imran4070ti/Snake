from turtle import Turtle, TurtleScreen
import os

HIGHSCORE_FILE_PATH = 'utils/scoresheet.txt'

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.high_score = self.get_high_score()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
    

    def update_score(self):
        self.score+=1
    
    def get_score(self):
        return self.score

    def display_score(self):
        self.write(f'Score: {self.score}\tHigh score: {self.high_score}', align=ALIGNMENT, font=FONT)
    
    def refresh_scoreboard(self):
        self.clear()
        self.display_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.refresh_scoreboard()

    def get_high_score(self):
        if not os.path.exists(HIGHSCORE_FILE_PATH):
            with open(HIGHSCORE_FILE_PATH, 'w') as file:
                file.write('0')
                file.close()
        highscore_file = open(HIGHSCORE_FILE_PATH, 'r')
        score = int(highscore_file.readline())
        highscore_file.close()
        return score
    
    def write_high_score(self):
        highscore_file = open(HIGHSCORE_FILE_PATH, 'w')
        highscore_file.write(str(self.high_score))
        highscore_file.close()

  

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align='center', font=('Arial', 50, 'normal'))

