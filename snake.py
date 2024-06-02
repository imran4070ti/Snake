from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0.0
UP = 90.0
LEFT = 180.0
DOWN = 270.0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        length = len(self.segments[:-1])
        for i in range(length):
            self.segments[length - i].goto(self.segments[length - i - 1].pos())
        self.segments[0].forward(MOVE_DISTANCE)
    
    def get_last_pos(self):
        return self.segments[-1].pos()
    
    def get_first_pos(self):
        return self.segments[0].pos()
    
    def get_heading(self):
        return self.segments[0].heading()

    def add_segment(self):
        last_pos = self.get_last_pos()
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(last_pos)
        self.segments.append(new_segment)

    def turn_left(self):
        if self.get_heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        
        # # Alternately
        # if self.get_heading() == UP:
        #     self.segments[0].left(90)
        # elif self.get_heading() == DOWN:
        #     self.segments[0].right(90)

    
    def turn_right(self):
        if self.get_heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def turn_up(self):
        if self.get_heading() != DOWN:
            self.segments[0].setheading(UP)

    def turn_down(self):
        if self.get_heading() != UP:
            self.segments[0].setheading(DOWN)

    def head(self):
        return self.segments[0]

    




