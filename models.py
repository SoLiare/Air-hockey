import arcade.key

PUCK = 50
PLAYER = 75
GOAL_UP = 616.5
GOAL_DOWN = 83.5
GOAL_LEFT = 0
GOAL_RIGHT = 800

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
        return (self.x-PUCK//2 <= GOAL_LEFT or self.x+PUCK//2 >= GOAL_RIGHT) and self.y >= GOAL_DOWN and self.y <= GOAL_UP

    def score(self):
        return self.x+PUCK//2 < GOAL_LEFT or self.x-PUCK//2 > GOAL_RIGHT


class Player1:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = []

    def start_point(self):
        self.x = 100
        self.y = self.world.height//2

    def add_direction(self, key, key_modifiers):
        if key==arcade.key.W:
            self.direction.append('up')
        if key==arcade.key.S:
            self.direction.append('down')
        if key==arcade.key.A:
            self.direction.append('left')
        if key==arcade.key.D:
            self.direction.append('right')

    def remove_direction(self, key, key_modifiers):
        if key==arcade.key.W:
            self.direction.remove('up')
        if key==arcade.key.S:
            self.direction.remove('down')
        if key==arcade.key.A:
            self.direction.remove('left')
        if key==arcade.key.D:
            self.direction.remove('right')

    def update(self, delta):
        for i in range(len(self.direction)):
            if self.direction[i]!='\n':
                if self.direction[i]=='up' and self.y < 533+83.5-PLAYER//2:
                    self.y+=5
                if self.direction[i]=='down' and self.y > 83.5+PLAYER//2:
                    self.y-=5
                if self.direction[i]=='left' and self.x > PLAYER//2:
                    self.x-=5
                if self.direction[i]=='right' and self.x < self.world.width//2-PLAYER//2:
                    self.x+=5


class Player2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = []

    def start_point(self):
        self.x = self.world.width-100
        self.y = self.world.height//2

    def add_direction(self, key, key_modifiers):
        if key==arcade.key.UP:
            self.direction.append('up')
        if key==arcade.key.DOWN:
            self.direction.append('down')
        if key==arcade.key.LEFT:
            self.direction.append('left')
        if key==arcade.key.RIGHT:
            self.direction.append('right')

    def remove_direction(self, key, key_modifiers):
        if key==arcade.key.UP:
            self.direction.remove('up')
        if key==arcade.key.DOWN:
            self.direction.remove('down')
        if key==arcade.key.LEFT:
            self.direction.remove('left')
        if key==arcade.key.RIGHT:
            self.direction.remove('right')

    def update(self, delta):
        for i in range(len(self.direction)):
            if self.direction[i]!='\n':
                if self.direction[i]=='up' and self.y < 533+83.5-PLAYER//2:
                    self.y+=5
                if self.direction[i]=='down' and self.y > 83.5+PLAYER//2:
                    self.y-=5
                if self.direction[i]=='left' and self.x > self.world.width//2+PLAYER//2:
                    self.x-=5
                if self.direction[i]=='right' and self.x < self.world.width-PLAYER//2:
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
        if self.puck.score():
            START = 0
            self.puck.start_point()
            self.player1.start_point()
            self.player2.start_point()
        else:
            START+=1

    def on_key_press(self, key, key_modifiers):
        self.player1.add_direction(key, key_modifiers)
        self.player2.add_direction(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.player1.remove_direction(key, key_modifiers)
        self.player2.remove_direction(key, key_modifiers)
