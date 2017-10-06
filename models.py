import arcade.key

PUCK = 50
PLAYER = 75

START = 0

class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Puck:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def start_point(self):
        self.x = self.world.width//2
        self.y = self.world.height//2

    def direction(self, keyX, keyY):
        if keyX==0 and keyY==0:
            self.keyX = 0
            self.keyY = 0
        else:
            if self.x==keyX:
                self.keyX = 0
            elif self.x > keyX:
                self.keyX = 5
            else:
                self.keyX = -5
            if self.y==keyY:
                self.keyY = 0
            elif self.y > keyY:
                self.keyY = 5
            else:
                self.keyY = -5

    def update(self, delta):
        if not self.goal():
            if self.x+PUCK//2 > self.world.width or self.x-PUCK//2 < 0:
                self.keyX = self.keyX*-1
            if self.y-PUCK//2 < 83.5 or self.y+PUCK//2 > 533+83.5:
                self.keyY = self.keyY*-1
        self.x+=self.keyX
        self.y+=self.keyY

    def hit(self, other, hit_size):
        return (abs(self.x-other.x)<=hit_size) and (abs(self.y-other.y)<=hit_size)

    def goal(self):
        return (self.x-37.5 > 800 or self.x+37.5 < 0) and (self.y-37.5 > 216.75 and self.y+37.5 < 483.25)


class Player1:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.key = '0'

    def start_point(self):
        self.x = 100
        self.y = self.world.height//2

    def direction(self, key):
        self.key = key

    def update(self, delta):
        if self.key!=0:
            if self.key=='w' and self.y < 533+83.5-PLAYER//2:
                self.y+=5
            if self.key=='s' and self.y > 83.5+PLAYER//2:
                self.y-=5
            if self.key=='a' and self.x > PLAYER//2:
                self.x-=5
            if self.key=='d' and self.x < self.world.width//2-PLAYER//2:
                self.x+=5


class Player2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.key = '0'

    def start_point(self):
        self.x = self.world.width-100
        self.y = self.world.height//2

    def direction(self, key):
        self.key = key

    def update(self, delta):
        if self.key!=0:
            if self.key=='up' and self.y < 533+83.5-PLAYER//2:
                self.y+=5
            if self.key=='down' and self.y > 83.5+PLAYER//2:
                self.y-=5
            if self.key=='left' and self.x > self.world.width//2+PLAYER//2:
                self.x-=5
            if self.key=='right' and self.x < self.world.width-PLAYER//2:
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
        global START
        if START==0:
            self.puck.direction(0,0)
        self.player1.update(delta)
        self.player2.update(delta)
        self.puck.update(delta)
        if self.puck.hit(self.player1, PLAYER//2+PUCK//2):
            self.puck.direction(self.player1.x, self.player1.y)
        if self.puck.hit(self.player2, PLAYER//2+PUCK//2):
            self.puck.direction(self.player2.x, self.player2.y)
        if self.puck.goal():
            START = 0
            self.puck.start_point()
            self.player1.start_point()
            self.player2.start_point()
        else:
            START+=1

    def on_key_press(self, key, key_modifiers):
        if key==arcade.key.W:
            self.player1.direction('w')
        if key==arcade.key.S:
            self.player1.direction('s')
        if key==arcade.key.A:
            self.player1.direction('a')
        if key==arcade.key.D:
            self.player1.direction('d')
        if key==arcade.key.UP:
            self.player2.direction('up')
        if key==arcade.key.DOWN:
            self.player2.direction('down')
        if key==arcade.key.LEFT:
            self.player2.direction('left')
        if key==arcade.key.RIGHT:
            self.player2.direction('right')

    def on_key_release(self, key, key_modifiers):
        if key==arcade.key.W or key==arcade.key.S or key==arcade.key.A or key==arcade.key.D:
            self.player1.direction('0')
        if key==arcade.key.UP or key==arcade.key.DOWN or key==arcade.key.RIGHT or key==arcade.key.LEFT:
            self.player2.direction('0')
