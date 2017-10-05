import arcade.key

class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Puck:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        if self.x > self.world.width:
            self.x = 0
        self.x+=5


class Player1:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.key = '0'

    def direction(self, key):
        self.key = key

    def update(self, delta):
        if self.key!=0:
            if self.key=='w' and self.y < 533+83.5-50:
                self.y+=5
            elif self.key=='s' and self.y > 83.5+50:
                self.y-=5
            elif self.key=='a' and self.x > 50:
                self.x-=5
            elif self.key=='d' and self.x < self.world.width//2-50:
                self.x+=5


class Player2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.key = '0'

    def direction(self, key):
        self.key = key

    def update(self, delta):
        if self.key!=0:
            if self.key=='up' and self.y < 533+83.5-50:
                self.y+=5
            elif self.key=='down' and self.y > 83.5+50:
                self.y-=5
            elif self.key=='left' and self.x > self.world.width//2+50:
                self.x-=5
            elif self.key=='right' and self.x < self.world.width-50:
                self.x+=5

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = Board(width // 2, height // 2)
        self.puck = Puck(self, width // 2, height // 2)
        self.player1 = Player1(self, 100, height // 2)
        self.player2 = Player2(self, width-100, height // 2)

    def update(self, delta):
        self.puck.update(delta)
        self.player1.update(delta)
        self.player2.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key==arcade.key.W:
            self.player1.direction('w')
        elif key==arcade.key.S:
            self.player1.direction('s')
        elif key==arcade.key.A:
            self.player1.direction('a')
        elif key==arcade.key.D:
            self.player1.direction('d')
        if key==arcade.key.UP:
            self.player2.direction('up')
        elif key==arcade.key.DOWN:
            self.player2.direction('down')
        elif key==arcade.key.LEFT:
            self.player2.direction('left')
        elif key==arcade.key.RIGHT:
            self.player2.direction('right')

    def on_key_release(self, key, key_modifiers):
        if key==arcade.key.W or key==arcade.key.S or key==arcade.key.A or key==arcade.key.D:
            self.player1.direction('0')
        elif key==arcade.key.UP or key==arcade.key.DOWN or key==arcade.key.RIGHT or key==arcade.key.LEFT:
            self.player2.direction('0')
