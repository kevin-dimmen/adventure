"""Handles base characters in the game."""

from __future__ import annotations

from typing import Optional
from typing import Tuple

import pygame
from loguru import logger

from adventure.constants import COLOR_WHITE
from adventure.entities.entity import Entity
from adventure.weapons.firearms import Firearm


class Character(Entity):
    """Base class for any character in the game."""

    COLOR = COLOR_WHITE
    DEFAULT_RADIUS = 25
    MOVEMENT_SPEED = 150
    MAX_HEALTH = 100

    def __init__(self, x: Optional[int] = 0, y: Optional[int] = 0, radius: Optional[int] = None):
        super().__init__(x, y, radius if radius is not None else self.DEFAULT_RADIUS)
        self.shot_cooldown = 0
        self.shot_cooldown_interval = 0.3
        self.health = self.MAX_HEALTH
        self.weapon = Firearm(self)

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
        if self.weapon:
            self.weapon.update_cooldown(dt)

    def move_forwards(self, dt) -> None:
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += velocity * self.movement_speed * dt

    def move_backwards(self, dt) -> None:
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += velocity * self.movement_speed / 2 * dt * -1

    def move_left(self, dt) -> None:
        return  # TODO figure out strafe logic
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += velocity * self.movement_speed / 2 * dt * -1

    def move_right(self, dt) -> None:
        return  # TODO figure out strafe logic
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += velocity * self.movement_speed / 2 * dt * -1

    def shoot(self, dt: int) -> None:
        if self.weapon:
            self.weapon.shoot()

    def is_facing_character(self, character: Character) -> bool:
        """Check if the current character is facing another character."""
        # TODO: fix top account for distance from character since distance affects angle buffer
        allowed_angle_buffer = 3
        angle_to_target = self.get_angle_to_vector(character.position)
        return abs(angle_to_target - self.rotation) < allowed_angle_buffer

    def target_character(self, character: Character, dt: int) -> None:
        """Turn this character towards a given character."""
        if character is not self:
            self.rotate_towards(dt, character.position)

    def receive_damage(self, projectile) -> None:
        self.health -= projectile.get_damage()
        if self.health < 0:
            self.die()

    def die(self) -> None:
        logger.info(f"{self.__class__.__name__} @ {id(self)} dies")
        self.kill()
