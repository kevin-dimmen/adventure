"""
Base class for any projectiles.
"""

import pygame

from adventure.entities.entity import Entity


class Projectile(Entity):
    """A shot from the player character."""

    MOVEMENT_SPEED = 500
    SHOT_RADIUS = 5
    SHOT_RANGE = 350
    DAMAGE_VALUE = 50

    def __init__(self, x, y, rotation, shooter):
        super().__init__(x, y, self.SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation)
        self.velocity *= self.MOVEMENT_SPEED
        self.origin = pygame.Vector2(x, y)
        self.range = self.SHOT_RANGE
        self.shooter = shooter
        self.damage_value = self.DAMAGE_VALUE

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def get_damage(self) -> float:
        return self.damage_value

    def check_range(self) -> None:
        """Kill the projectile if it has maximized its range."""
        if self.origin.distance_to(self.position) > self.range:
            self.kill()

    def check_hit(self, other) -> None:
        """Check if this projectile hits something."""
        if other is self.shooter:
            return
        if self.check_collision(other):
            other.receive_damage(self)
            self.kill()
