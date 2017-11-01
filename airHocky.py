import arcade

from models import World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()
    

class AHwindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.board = ModelSprite('board.png', model=self.world.board)
        self.board.set_position(width // 2, height // 2)

        self.puck = ModelSprite('puck.png', model=self.world.puck)
        self.puck.set_position(width // 2, height // 2)

        self.player1 = ModelSprite('player1.png', model=self.world.player1)
        self.player1.set_position(100, height // 2)

        self.player2 = ModelSprite('player2.png', model=self.world.player2)
        self.player2.set_position(width-100, height // 2)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)
 
    def on_draw(self):
        arcade.start_render()
        self.board.draw()
        self.puck.draw()
        self.player1.draw()
        self.player2.draw()

        arcade.render_text(arcade.create_text(str(self.world.player1_score)+" : "+str(self.world.player2_score), arcade.color.WHITE, 20), 380, 50)
    
    def update(self, delta):
        self.world.update(delta)
        

def main():
    window = AHwindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__=='__main__':
    main()
