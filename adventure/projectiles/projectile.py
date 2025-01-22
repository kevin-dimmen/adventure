"""
Base class for any projectiles.
"""

import pygame

from adventure.entities.entity import Entity


class Projectile(Entity):
    """A shot from the player character."""

    SHOOT_SPEED = 500
    SHOT_RADIUS = 5
    SHOT_RANGE = 350

    def __init__(self, x, y, rotation):
        super().__init__(x, y, self.SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation)
        self.velocity *= self.SHOOT_SPEED
        self.origin = pygame.Vector2(x, y)
        self.range = self.SHOT_RANGE

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def check_range(self) -> None:
        """Kill the projectile if it has maximized its range."""
        if self.origin.distance_to(self.position) > self.range:
            self.kill()
