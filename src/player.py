import arcade
from config import TILE, SCREEN_W, SCREEN_H

MOVE_SPEED = 6

class Player:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

        self.dx = 0
        self.dy = 0

        self.radius = TILE // 2 - 2

    def on_key_press(self, key):
        if key == arcade.key.UP:
            self.dx = 0
            self.dy = MOVE_SPEED
        elif key == arcade.key.DOWN:
            self.dx = 0
            self.dy = -MOVE_SPEED
        elif key == arcade.key.LEFT:
            self.dx = -MOVE_SPEED
            self.dy = 0
        elif key == arcade.key.RIGHT:
            self.dx = MOVE_SPEED
            self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < self.radius:
            self.x = self.radius
        if self.x > SCREEN_W - self.radius:
            self.x = SCREEN_W - self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > SCREEN_H - self.radius:
            self.y = SCREEN_H - self.radius

    def draw(self):
        arcade.draw_circle_filled(
            self.x,
            self.y,
            self.radius,
            arcade.color.YELLOW
        )
