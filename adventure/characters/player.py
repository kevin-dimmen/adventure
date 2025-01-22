"""Handle the player character."""

from typing import Optional
from typing import Tuple

import pygame

from adventure.characters.character import Character

PLAYER_SPEED = 200
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300


class Player(Character):

    DEFAULT_RADIUS = 20

    def triangle(self) -> Tuple[int, int, int]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return a, b, c

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, self.color, self.triangle(), self.width)

    def update(self, dt) -> None:
        self.shot_cooldown -= dt
        self.look_towards_mouse(dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if pygame.mouse.get_pressed()[0]:
            self.shoot(dt)

    def look_towards_mouse(self, dt: int) -> None:
        self.rotate_towards(dt, self.get_mouse_position())

    def move(self, dt) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
