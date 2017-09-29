import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class AHwindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)


def main():
    window = AHwindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__=='__main__':
    main()
