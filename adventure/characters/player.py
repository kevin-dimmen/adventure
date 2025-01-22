"""Handle the player character."""

from typing import Optional

import pygame

from adventure.characters.character import Character
from adventure.exceptions import GameExit
from adventure.weapons.firearms import SMG


class Player(Character):

    DEFAULT_RADIUS = 20
    TURN_SPEED = 300
    MOVEMENT_SPEED = 200
    MAX_HEALTH = 250

    def __init__(self, x: Optional[int] = 0, y: Optional[int] = 0, radius: Optional[int] = None):
        super().__init__(x, y, radius)
        self.weapon = SMG(self)

    def update(self, dt) -> None:
        super().update(dt)

        self.look_towards_mouse(dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_forwards(dt)
        if keys[pygame.K_s]:
            self.move_backwards(dt)
        if keys[pygame.K_a]:
            self.move_left(dt)
        if keys[pygame.K_d]:
            self.move_right(dt)

        if pygame.mouse.get_pressed()[0]:
            self.shoot(dt)

    def look_towards_mouse(self, dt: int) -> None:
        self.rotate_towards(dt, self.get_mouse_position())

    def kill(self) -> None:
        super().kill()
        raise GameExit()
