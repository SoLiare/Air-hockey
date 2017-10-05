class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Puck:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, delta):
        if self.x > self.wolrd.width:
            self.x = 0
        self.x+=5


class Player1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, delta):
        if self.x > self.wolrd.width:
            self.x = 0
        self.x+=5


class Player2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, delta):
        if self.x > self.wolrd.width:
            self.x = 0
        self.x+=5
    

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = Board(width // 2, height // 2)
        self.puck = Puck(width // 2, height // 2)
        self.player1 = Player1(100, height // 2)
        self.player2 = Player2(width-100, height // 2)

    def update(self, delta):
        self.puck.update(delta)
        self.player1.update(delta)
        self.player2.update(delta)
