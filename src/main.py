import arcade
from config import SCREEN_W, SCREEN_H, TITLE
from player import Player

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_W, SCREEN_H, TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.player = Player(SCREEN_W // 2, SCREEN_H // 2)

    def on_draw(self):
        self.clear()
        self.player.draw()

    def on_update(self, delta_time):
        self.player.update()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

def main():
    Game()
    arcade.run()

if __name__ == "__main__":
    main()
