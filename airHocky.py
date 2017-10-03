import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

class AHwindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.board_sprite = arcade.Sprite('board.png')
        self.board_sprite.set_position(width // 2, height // 2)

    def on_draw(self):
        arcade.start_render()
        self.board_sprite.draw()

def main():
    window = AHwindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__=='__main__':
    main()
