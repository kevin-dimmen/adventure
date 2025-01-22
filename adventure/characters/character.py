"""Handles base characters in the game."""

from __future__ import annotations

from typing import Optional

from adventure.constants import COLOR_WHITE
from adventure.entities.entity import Entity
from adventure.projectiles.projectile import Projectile


class Character(Entity):
    """Base class for any character in the game."""

    COLOR = COLOR_WHITE
    DEFAULT_RADIUS = 50

    def __init__(self, x: Optional[int] = 0, y: Optional[int] = 0, radius: Optional[int] = None):
        super().__init__(x, y, radius if radius is not None else self.DEFAULT_RADIUS)
        self.width = 2
        self.shot_cooldown = 0
        self.shot_cooldown_interval = 0.3

    def shoot(self, dt: int) -> None:
        if self.shot_cooldown > 0:
            return
        Projectile(self.position.x, self.position.y, self.rotation)
        self.shot_cooldown = self.shot_cooldown_interval
